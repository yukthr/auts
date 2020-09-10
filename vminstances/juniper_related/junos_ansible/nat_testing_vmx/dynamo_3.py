import boto3
import datetime
import yaml
import time
from boto3.dynamodb.conditions import Key, Attr
import sys
import yaml
from jinja2 import Template
import os
import json


dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

table = dynamodb.Table('new_table')
table.load()

"""
response = table.query(KeyConditionExpression=Key('Public_IP').eq('887.0.0.1'))
>>> response
{u'Count': 1, u'Items': [{u'Public_IP': u'887.0.0.1'}], u'ScannedCount': 1, 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '9T6I34LP0JKN2BF2E5QNT4C7FRVV4KQNSO5AEMVJF66Q9ASUAAJG',
'HTTPHeaders': {'x-amzn-requestid': '9T6I34LP0JKN2BF2E5QNT4C7FRVV4KQNSO5AEMVJF66Q9ASUAAJG', 'content-length': '70', 'server': 'Server', 'connection': 'keep-alive',
'x-amz-crc32': '2093029419', 'date': 'Mon, 04 Feb 2019 17:20:02 GMT', 'content-type': 'application/x-amz-json-1.0'}}}

"""

def response_data(Public_IP):
    response = table.query(KeyConditionExpression=Key('Public_IP').eq(Public_IP))
    if response['Count'] == 1:
        return 'IP Already Exists! \n\n{}'.format(response)
    else:
        print('Good to Proceed with NAT Entry')
        generate_config(build_yaml())


def build_yaml():
    # Build pulic ip , private ip and host to which config needs to be deployed to
    yaml_for_this_build = dict(pu_ip = Public_IP, pi_ip = Private_IP, host_name = Device)
    file_yaml = 'yaml_for_this_build_{}.yml'.format(dt_iso)  # type: str
    with open(file_yaml, 'w') as outfile:
        yaml.dump(yaml_for_this_build, outfile, default_flow_style=False)
    return file_yaml


def generate_config(build_yaml):
    with open(build_yaml, 'r') as yamlfile:
        yaml_data = yaml.load(yamlfile.read())

    with open("nat_deploy.j2", 'r') as jinjafile:
        jinja_data = jinjafile.read()
        template = Template(jinja_data)

    final_config_gen = template.render(yaml_data)
    file_final = 'final_config_{}'.format(dt_iso)
    with open(file_final,'w') as file:
        for line in final_config_gen:
            file.write(line)
    print(final_config_gen)

    print("Uploading yaml file to s3 {}".format(build_yaml))
    s3.upload_file(build_yaml, "nattranslations", build_yaml)
    print("Uploading final config generated to s3 {}".format(file_final))
    s3.upload_file(file_final, "nattranslations", file_final)
    #upload verification
    print("print sleeping 10 seconds")
    time.sleep(10)
    print("Verifying if s3 object upload was successful ")
    #use try except
    response1 = s3.get_object(Bucket='nattranslations',Key=build_yaml)
    response2 = s3.get_object(Bucket='nattranslations',Key=file_final)
    if response1['ResponseMetadata']['HTTPStatusCode'] == 200 and response2['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('S3 verification successful.proceeding with deployment')
        invoke_ansible(y=file_final)
    else:
        print('S3 verification failed. Upload probably failed. Exception occured')
        sys.exit(1)
    return file_final

def invoke_ansible(y=None):

    print(y)
    generate_ansible_yml = 'junos_base_junos_config_deploy_{}'.format(dt_iso)
    change_jinja = "sudo sed 's/test.conf/{}/g' base_junos_config_deploy.yml > {}".format(y,generate_ansible_yml)
    os.system(change_jinja)


    ansible_command = 'sudo ansible-playbook -i hosts {}'.format(generate_ansible_yml)
    os.system(ansible_command)
    with open('output','r') as file:
        json_output = json.load(file)
        if json_output['failed'] == False and json_output['changed']== True:
            print("Ansible successfully deployed the configuration. Verified from output Debug File.")
            print("Updating DynamoDB")
            print("Uploading ansible yaml file to s3 {}".format(generate_ansible_yml))
            s3.upload_file(generate_ansible_yml, "nattranslations", generate_ansible_yml)
            print("uploading ansible output to s3")
            s3.upload_file('output', "nattranslations", 'output_{}'.format(dt_iso))
            final_update_dynamo()
            cleanup(build_yaml())
            os.system('rm -rf {}'.format(generate_ansible_yml))
            os.system('rm -rf {}'.format(y))
        else:
            print("Ansible failed! Aborting")
            cleanup(build_yaml())
            os.system('rm -rf {}'.format(generate_ansible_yml))
            sys.exit(1)

    #Upload ansible yaml to s3 and also diff to s3



def final_update_dynamo():
    #update the DB table back with the public IP
    response = table.put_item(TableName='new_table', Item={'Public_IP': '{}'.format(Public_IP)})
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Update completed successfully, Received HTTPStatusCode 200")
        print("\n Update of public IP on the device completed and DB updated")
    else:
        print("update was not complted. Rolling back the changes on the Device, Consult NE team")
        print("Here we will use ansible to rollback ")



def cleanup(y):
    print('cleaning up file: output')
    print('cleaning up file: generate_ansible_yml')
    os.system('rm -rf output ')
    os.system('rm -rf {}'.format(y))

if __name__ == "__main__":
    Public_IP = input('Enter the Public IP: ')
    Private_IP = input('Enter the Private IP: ')
    Device  = input('Device for the config to be deployed: eg: r1-seattle-core: ')

    dt_iso = datetime.datetime.now().isoformat()
    response_data(Public_IP)



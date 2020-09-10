import boto3
import yaml
import time
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

table = dynamodb.Table('new_table')
table.load()


Public_IP = input('Enter the Public IP: ')
Private_IP = input('Enter the Private IP: ')
Device  = input('Device for the config to be deployed: eg: r1-seattle-core: ')

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
        print('IP Already Exists! \n\n{}'.format(response))
    else:
        print('Good to Proceed with NAT Entry')
        push_s3(build_yaml())


def build_yaml():
    # Build pulic ip , private ip and host to which config needs to be deployed to
    yaml_for_this_build = dict(pu_ip = Public_IP, pi_ip = Private_IP, host_name = Device)
    file = 'yaml_for_this_build_{}.yml'.format(time.ctime())  # type: str
    with open(file, 'w') as outfile:
        yaml.dump(file, outfile, default_flow_style=False)
    return file

def push_s3(build_yaml):
    print("Uploading files to s3 {}".format(build_yaml))
    s3.upload_file(build_yaml, "nattranslations", build_yaml)


response_data(Public_IP)


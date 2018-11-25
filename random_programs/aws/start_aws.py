
# Script to power on and power off aws-instances. Make sure to run aws configure and set your account before executing this script. Also, boto3 aws package should be# installed

import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

# Required output will be in 'Reservations'

output = response['Reservations']

# calculate the length of the output rather list

instance_ids = [] # This is an empty list of instances

for i in range(len(output)):
    instance_ids.append(output[i]['Instances'][0]['InstanceId'])

def poweron():
    #This currently powers on ubuntu and vsrx
    for i in instance_ids:
        try:
            response_out = ec2.start_instances(InstanceIds=[i], DryRun=False)
            print(response_out)
        except ClientError as e:
            print(e)

def poweroff():
    #This powers off ubuntu and srx
    for i in instance_ids:
        try:
            response_out = ec2.stop_instances(InstanceIds=[i], DryRun=False)
            print(response_out)
        except ClientError as e:
            print(e)

if str.lower(sys.argv[1]) == 'on':
	poweron()
elif str.lower(sys.argv[1]) == 'off':
        poweroff()
else:
	print("Key words supported on and off! exiting")
	sys.exit(1)


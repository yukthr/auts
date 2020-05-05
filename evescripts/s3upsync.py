# you have to setup the your host with AWS credentials,they can be found in lastpass with network-llama 

# This will be a cron job to sync with s3 bucket regularly


import sys
import subprocess
import argparse


parser = argparse.ArgumentParser(description='Upload and sync local directory with Remote S3 Bucket')
parser.add_argument('-b', action='store',dest='bucketname',help='Pass the remote s3 bucketname ',type=str,required=True)
parser.add_argument('-p', action='store',dest='pathname',help='Pass the Local Directory Path Name to sync',type=str,required=True)
args = parser.parse_args()

bucketname = args.bucketname
pathname   = args.pathname

def s3upload():
    try:
        print('uploading to S3')
        output_bytes = subprocess.check_output(['sudo','aws','s3','sync',f'{pathname}',f's3://{bucketname}'])
        print(output_bytes.decode('utf-8').strip())
        print('finished uploading to s3')
    except:
        print('Some error occured, Please try again')

s3upload()

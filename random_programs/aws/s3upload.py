import sys
import subprocess


def s3upload(filetoupload, s3uri):
    try:
        print('uploading to S3')
        output_bytes = subprocess.check_output(['sudo','aws','s3','cp',filetoupload, s3uri])
        print(output_bytes.decode('utf-8').strip())
        print('finished uploading to s3')
    except:
        print('Some error occured, Please try again')

#s3upload('/root/vmlinuz-4.15.0-1061-gcp','s3://evengrakesh')

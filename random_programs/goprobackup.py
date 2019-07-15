from goprocam import GoProCamera, constants
import boto3
import os
import time

str1 = time.ctime().split(' ')
create_dir = str1[1]+str1[3]+''.join(str1[4].split(':'))
os.system('mkdir {}'.format(create_dir))
os.chdir(create_dir)


def get_files_from_gopro():

    gpCam = GoProCamera.GoPro()
    try:
        gpCam.downloadAll()
    except:
        print("Looks like an error")
        get_files_from_gopro()


def upload_s3(filename,create_dir):

    try:
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(filename,'gopro-rakesh-backup',create_dir/filename)
    except:
        print("Looks like an error")
        upload_s3(filename,crate_dir)



get_files_from_gopro()

@ we have to get all the files as a list and then create a concurrent upload function for this to happen fast.




#os.chdir('../')
#os.system('tar -cvzf {}.tar.gz {}'.format(create_dir,create_dir))

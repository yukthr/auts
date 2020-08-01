from s3upload import s3upload
import glob
import os
import concurrent.futures
import time

os.chdir('/root/images/IOS')



list_of_files = glob.glob('*')
s3uri = 's3://evengrakesh'

start = time.perf_counter()


with concurrent.futures.ThreadPoolExecutor() as executor:

        results = [executor.submit(s3upload, file_name, s3uri) for file_name in list_of_files]

        for f in concurrent.futures.as_completed(results):
                print(f.result())

finish = time.perf_counter()
print(finish-start)


# script to remove the inactive docker runtimes

import os
import logging 
import pandas as pd

logging.basicConfig(level=logging.INFO)


docker_get = os.system('sudo docker ps -a > dockeroutput.txt')

# Block to read file and conver to CSV

text_read = pd.read_fwf('dockeroutput.txt')

# Convert text file to csv 

text_read.to_csv('dockeroutput.csv')


pd_readfile = pd.read_csv('dockeroutput.csv',header=None)


def remove_dockerruns():
    if len(pd_readfile[1]) > 1:
        for i in pd_readfile[1][1:]:
            try:
                os.system('sudo docker rm {}'.format(i))
                logging.info('Removed instance ID - {}'.format(i))
            except:
                logging.info('Exception detected')
    else:
        logging.info('None of the images are running')

if __name__ == "__main__":
    remove_dockerruns()


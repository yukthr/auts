# The Program is intended to get a pcap file from router and open wireshark for the pcap

from jnpr.junos import Device as dev
from jnpr.junos.utils.ftp import FTP as ftp
import os
import sys
import logging

d = dev(user='lab', password='lab123', host='192.168.0.91')
d.open()
print(f"\nConnected to Device : {d.facts['hostname']} \n")

class FileWireshark:

    def __init__(self):
        file_to_get = input('Enter the filename: ')
        self.file_to_get = file_to_get


    def file_to_fetch(self):
        with ftp(d) as ftpd:
            self.ftp_file = ftpd.get(f'{self.file_to_get}', local_path=f'/Users/r/PycharmProjects/juniper/{self.file_to_get}')
            if not self.ftp_file:
                logging.error(msg="\nNo File Found!")
            else:
                print()
                print("\nFile transfer done! ")
            return self.ftp_file

    def wireshark(self):
        if self.ftp_file is True:
            os.system(f'\nwireshark {self.file_to_get}')
            sys.exit(1)
        else:
            logging.error(msg="\nWireshark cannot be Executed! ")
            sys.exit(1)


getfile = FileWireshark()
getfile.file_to_fetch()
getfile.wireshark()


import os
import time
import paramiko
from paramiko import AuthenticationException
from paramiko import SSHClient
from jnpr.junos import Device as dev
from jnpr.junos.utils.scp import SCP
import sys

# SSH Parameters

ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

class Ssh_Conn:

    def __init__(self, ip=sys.argv[1], interface=sys.argv[2]):
        self.ip = ip
        self.interface = interface
        self.command = "monitor traffic interface {} no-resolve write-file traffic-capture.pcap ".format(self.interface)


    def connect(self, num_retries=15):
        retry = 0
        while retry < num_retries:
            try:
                print('Connecting to {} and initiating capture on interface {} for 10 seconds '.format(self.ip,self.interface))
                ssh.connect(self.ip, port=22, username='lab', password='lab123', look_for_keys=False,
                            auth_timeout=20, allow_agent=False, timeout=10)
                stdin, stdout, stderr = ssh.exec_command(self.command)
                time.sleep(10)
                ssh.close()
                output = stdout.read()
                return output.decode("utf-8")
            except AuthenticationException:
                print('Encountered Error in connection Will retry in 5 seconds')
                time.sleep(5)


    def get_file(self):
        d = dev(host=self.ip, user='lab', password='lab123').open()
        with SCP(d) as scp:
            print("Fetching file - traffic-capture.pcap")
            scp.get('traffic-capture.pcap')
            print('Fetch Done!')

    def open_wireshark(self):
        os.system('wireshark {} &'.format('traffic-capture.pcap'))

r = Ssh_Conn()
r.connect()
r.get_file()
r.open_wireshark()
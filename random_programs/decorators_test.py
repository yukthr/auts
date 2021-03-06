import argparse
from jnpr.junos import Device

parser = argparse.ArgumentParser()
parser.add_argument('ip',help='Provide Ip address of the Juniper Device')
args = parser.parse_args()

ip = args.ip

# Decorator Function to handle connection and Return output
def connection_handler(fname):

    def device_connection(*args,**kwargs):
        d = Device(host=ip,user='lab',password='lab123')
        d.open()
        output = d.facts
        return fname(output=output,*args,**kwargs)

    return device_connection

@connection_handler
def get_reinfo(output=None):
    print(output['re_info'])


@connection_handler
def get_modelinfo(output=None):
    print(output['model_info'])


get_reinfo()
get_modelinfo()

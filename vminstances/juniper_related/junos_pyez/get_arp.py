#This program gets the arp addresses for the device
from jnpr.junos import Device as d
from jnpr.junos.op.arp import ArpTable as at #This get the arp table

dev = d(host="192.168.48.91",user='lab',passwd='lab123')
dev.open()

arp_list = at(dev).get() # at is the short form of ArpTable at the top

#Lets print out IP addresses available and ARP Entries

for arp in arp_list:
    print("\n{} via {} has arp {}").format(arp.ip_address,arp.interface_name,arp.mac_address)

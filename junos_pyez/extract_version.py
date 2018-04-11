#This program extracts version from the list of Devices and checks if it is great than 15.1
from jnpr.junos import Device as d #import Device Module for connectivity for ease
import re
list_of_devices = ['192.168.0.91','192.168.0.92']
for ip in list_of_devices:
	device = d(host='192.168.0.91',user="lab",password="lab123") # Just to make life easier in lab
	try:
		device.open()
	except:
		print("Could not connect! check the connectivity for {}".format(ip))
	output = device.facts #Collects facts form the device 
	version = output['version']
	if float((re.search(r"\d+.\d",version).group())) > 15.1 : #Basically output is a Dict and we are extracting value
		print("\nDevice {} is Running {} and above 15.1").format(ip,version)
	else:
		print("\nDevice {} is Running {} and below 15.1").format(ip,version)

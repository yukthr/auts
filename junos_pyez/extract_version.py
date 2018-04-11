#Thiss program extracts version from the list of Devices and checks if it is great than 15.1
from jnpr.junos import Device as d #import Device Module for connectivity for ease
import re #To import search functions module 
import logging #Just to indicate warning when not connected to device. 

list_of_devices = ['192.168.0.81','192.168.92']


""" #First am defning the function to check the condition if > 15.1 or not, bascially i could have done without writing this but try and except 
block become easy in this case """

def version_check(ouptput):
        version = output['version']

        if float((re.search(r"\d+.\d",version).group())) > 15.1 : #Basically output is a Dict and we are extracting value
                print("\nDevice {} is Running {} and above 15.1").format(ip,version)
        else:
                print("\nDevice {} is Running {} and below 15.1").format(ip,version)


for ip in list_of_devices:
    device = d(host=ip, user="lab", password="lab123")  # Just to make life easier in lab
    try:			#This helps to try the device IP and display a Error message cleanly
        device.open()
    except:
	print("\n")
        logging.warning("Error connecting to device")
    try:			#This helps to validate if the facts were collected cleanly or not 
        output = device.facts  # Collects facts form the device
        version_check(output)
    except:
       print("\nError fetching output from the Device {}".format(ip))


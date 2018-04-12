#This program aims at getting the list of routes available on the device
from jnpr.junos import Device as d
from jnpr.junos.op.routes import RouteTable #Module to import Route-table

#Make the connection to the device and open the device

dev = d(host='192.168.0.92',user='lab',password='lab123')
dev.open()

#Get the RouteTable and assign to a variable

routes = RouteTable(dev).get() # Get method will help you pull the routes

#Basically, you got the dictionary, the simplest way to get the routes is routes.keys()
#To get the routes in the linear fashion

for i in routes.keys():
    print i


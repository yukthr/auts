#Prrgram to Power-on VMware Instances 

import os # Importing to execute system wide commands
import time # Importing this as there is a sleep task
vm = [4,5,6,7,50] #Vmx instances and Ubuntu server
class vmware:
    def __init__(self,vmnumber):
        self.vmnumber = vmnumber
    def vmware_poweron(self):
         for i in self.vmnumber:
              vmware_poweron = "vim-cmd vmsvc/power.on {}".format(i)
              print "powering on instance {}".format(i)
              os.system(vmware_poweron)
              print "\n"
    def vmware_getstatus(self):
         for i in self.vmnumber:
              vmware_getstatus = "vim-cmd vmsvc/power.getstate {}".format(i)
              print "gettting state for instance {}".format(i)
              os.system(vmware_getstatus)
              print "\n"
vmware(vm).vmware_poweron()
print "\n"
time.sleep(10)
vmware(vm).vmware_getstatus()

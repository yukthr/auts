#This generates some sample data randomly for a interface flap 
import random
s = 'Apr  9 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1'
l = s.split(" ")
for i in range(20):
    i = i+1
    if i < 20:
        list2 = list(l)
        list2[2] = str(random.randint(9,15))
        print " ".join(list2)
        

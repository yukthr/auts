#Sample program to analylze the interface flaps from the logs

import matplotlib.pyplot as plt #This helps us to plot the data
import cStringIO #This helps us to convert stirng to list

#I found the below program good to generate the model data

import random
s = 'Apr  9 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1'
l = s.split(" ")
for i in range(21):
    i = i+1
    if i < 20:
        list2 = list(l)
        list2[2] = str(random.randint(9,15))


# From the data generated above, imagining that we got the data from the log file, lets do some analysis

collected_from_logs = """

Apr  14 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  14 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  11 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  15 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  15 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  9 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  14 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  10 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  15 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  9 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  12 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  15 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  13 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  11 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  15 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  13 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  10 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  9 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  13 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1
Apr  16 12:41:18  vMX-2 mib2d[4086]: SNMP_TRAP_LINK_DOWN: ifIndex 550, ifAdminStatus up(1), ifOperStatus down(2), ifName ae1

"""

# Below code would declare an empty list, basically am analyzing the day, you can extend it to the point where you can start with hour as well.

list_of_dates_flapped = []
lstr = collected_from_logs.strip()

for line in cStringIO.StringIO(collected_from_logs.strip()): #cStringIO.cStringIO is an intresting function and made my life easier to convert string to list
    print line.split()
    list_of_dates_flapped.append(int(line.split()[1])) #Basically here am adding the date which is index-1 after splitting the list
    # Sample list ['Apr', '14', '12:41:18', 'vMX-2', 'mib2d[4086]:', 'SNMP_TRAP_LINK_DOWN:', 'ifIndex', '550,', 'ifAdminStatus', 'up(1),', 'ifOperStatus', 'down(2),', 'ifName', 'ae1']


#Below is for graphing, please do remember you need to have matplotlib package installed.

plt.xlabel("Interface ae1 Flap day")
plt.ylabel("Number of times ae1 flapped")
plt.hist(list_of_dates_flapped,bins=30)
plt.show()

#End of the program 

# To display the bus times and also announce them
import os
import urllib2
import json
import numpy as np
from matplotlib import pyplot as pt
duetime = [] #Declaring Empty list for some graph analysis
#14 Auburn - stop 527
urla = 'http://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=610&format=json'
#reading the url data
url_read = urllib2.urlopen(urla).read()
#convert to json
url_json = json.loads(url_read)
#values are stored in results variable - this is all Dict
for i in url_json['results']:
    duetime.append(float(str(i['duetime'])))
    print("Bus {} in {} Minues").format(str(i['route']),str(i['duetime']))
print duetime
for i in duetime:
	if i < 15.0 and i > 10.0:
		os.system("omxplayer -o alsa /home/pi/B10.m4a")
#some graphical analysis - histogram vs time
#convert list to numpylist for plotting
np_duetime = np.array(duetime)
#plot as hist
try:
     pt.xlabel("Due Time")
     pt.ylabel("Frequency")
     pt.hist(np_duetime,bins=500)
except:
     print("No Buses Available! ")
pt.show()
pt.close()

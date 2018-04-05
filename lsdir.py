import os
import subprocess
#l = os.system("ls | egrep -i sample")
proc = subprocess.Popen('ls | egrep -i sample',stdout=subprocess.PIPE,shell=True)
output = proc.stdout.read()
directories = output.split()

"""

for i in directories:
	print "Program Start"
	os.system("python {}/*.py".format(i))
"""

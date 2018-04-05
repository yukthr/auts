import os
import subprocess
#l = os.system("ls | egrep -i sample")
proc = subprocess.Popen('ls | egrep -i sample',stdout=subprocess.PIPE,shell=True)
output = proc.stdout.read()
directories = output.split()
print directories
for i in directories:
	print "Program Start"
	print i
	os.system("python {}/*.py").format(i)

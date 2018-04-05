import os
import subprocess
#l = os.system("ls | egrep -i sample")
proc = subprocess.Popen('ls | egrep -i sample',stdout=subprocess.PIPE)
output = proc.stdout.read()
print output


# The goal of this program is to analyze the output.txt and get a list of vms which are currently powered on for my later use-case

# To do this i will be using pandas

import pandas as pd
import numpy  as np


# First we need to have the output.txt read and may be convert it to something simple for our operations - csv

read_output = pd.read_fwf('output.txt')

#Once this is read, we will convert it to csv

read_output.to_csv('output.csv')

#Once we have csv file, we will read into the csv file.

df = pd.read_csv('output.csv', header=None) #Am not including any headers

# Lets make a dictionary out of two useful pieces 1.name and 1.vmid, if you observe closely, you will see them under column named [1] and [6]

#pandas offers fantastic fleixibility in combining these two

df_vmid = df[1]
df_os   = df[6]


#For anything useful lets make a dictionary out of these two pandas dataframes

dict_vmos = {}



# I have used a Try Except block becuse i realized, it was also giving us osFile:vimid as key value pair so just to eliminate this am checking for an Integer


for i,j in zip(df_vmid, df_os):
 try:
  if int(i) > 0:
   dict_vmos[i] = j
 except:
  continue

print("\n")
print(" Dictionary for df[1] and df[6]")
print("\n")
print(dict_vmos)

print("\n")

# Lets print and see how this looks like
for i in dict_vmos.keys():
  command = 'vim-cmd vmsvc/power.getstate {}'.format(i)
  print(command)

# To Analyze data efficiently from a CSV file, which is a typical format
# Requirement - To filter out which DataCenter devices has RMA from a list of devices
# For anyone not faimilar with these packages, just understand the use case vs traditional looping / and having Data in Lists / Dicts 

import pandas as pd # Pandas package is used to analyze the data by converting them into rectangular array
import numpy as np #Numpy package is similar to pandas except for the facts it supports 2D array, we need this to write our boolean logic for yes/no as you will see 

df = pd.read_csv('rma_status.csv')

#Sample output 

"""

>>> df
   Devices    LC RMA_Status
DC
1       r1  abcx        yes
2       r2  abca         no
2       r3  abcb         no
6       r4  abcd        yes
4       r5  abcz        yes
5       r6  abcy         no
7       r5  abcn        yes
1       r1  abcx        yes
2       r2  abca         no
2       r3  abcb         no
6       r4  abcd        yes
4       r5  abcz        yes
5       r6  abcy         no
7       r5  abcn         no
1       r1  abcx        yes
2       r2  abca         no
2       r3  abcb         no
6       r4  abcd        yes
4       r5  abcz         no
5       r6  abcy         no
7       r5  abcn        yes
1       r1  abcx        yes
2       r2  abca         no
2       r3  abcb        yes
6       r4  abcd        yes
4       r5  abcz         no
5       r6  abcy         no
7       r5  abcn        yes
1       r1  abcx         no
2       r2  abca         no
2       r3  abcb         no
6       r4  abcd        yes
4       r5  abcz         no
5       r6  abcy         no
7       r5  abcn        yes

"""

# From the above output we need to know which devices has status marked yes 

#Let make a numpy array which has boolean True / False for values 'yes' and 'no'

df_nparray  = np.array(df['RMA_Status']=='yes') #This will give us a Bool list of Yes/No 

#Sample output 

"""

>>> df_nparray
array([ True, False, False,  True,  True, False,  True,  True, False,
       False,  True,  True, False, False,  True, False, False,  True,
       False, False,  True,  True, False,  True,  True, False, False,
        True, False, False, False,  True, False, False,  True])

"""

# Now the easy step, just have this df_nparray point as a Boolean to our df which will give the values only for True 

print(df[df_nparray])

"""

>>> print(df[df_nparray])
   Devices    LC RMA_Status
DC
1       r1  abcx        yes
6       r4  abcd        yes
4       r5  abcz        yes
7       r5  abcn        yes
1       r1  abcx        yes
6       r4  abcd        yes
4       r5  abcz        yes
1       r1  abcx        yes
6       r4  abcd        yes
7       r5  abcn        yes
1       r1  abcx        yes
2       r3  abcb        yes
6       r4  abcd        yes
7       r5  abcn        yes
6       r4  abcd        yes
7       r5  abcn        yes

"""

#It becomes extremely easy when you have pandas and numpy covert data for analaysis vs regurlar list and looping through the list 

        





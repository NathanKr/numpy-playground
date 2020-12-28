import numpy as np
import time
import sys

numItems = 100000
l = list(range(numItems)) # list of integer 0,1,2, .....,999
someInteger = 4
print("memory size list : ",sys.getsizeof(someInteger)*numItems) 

array = np.arange(numItems)
print("memory size numpy array : ",numItems*array.itemsize) 

sum=0
index=0
start = 1000*time.time()

while index < numItems:
    l[index] = l[index]*2
    index += 1


stop = 1000*time.time()
print("total time -> multiply by a scalar for list [mSec] : ",stop-start)

start = 1000*time.time()
array = array*2
stop = 1000*time.time()
print("total time -> multiply by a scalar for array [mSec] : ",stop-start)

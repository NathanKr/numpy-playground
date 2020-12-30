import numpy as np

m=10
ar1 = np.arange(m)
print("ar1 befor\n",ar1)
ar2 = 5* np.ones(m)

# replace all items above 5 by 10
ar1 = np.where(ar1 > 5 ,ar2, ar1)
print("ar1 after\n",ar1)

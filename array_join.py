import numpy as np

ar1 = np.array([1,2,3,4])
ar2 = np.array([6,6,7,8])
ar3 = np.concatenate((ar1,ar2)) # default is axis = 0 
print(ar3)

m1 = np.array([[1 , 2] , [3 , 4]])
m2 = np.array([[5 , 6] , [7 , 8]])
m3 = np.concatenate((m1,m2)) # default is axis = 0 
print("m3\n",m3)

m4 = np.concatenate((m1,m2),axis=1)
print("m4\n",m4)

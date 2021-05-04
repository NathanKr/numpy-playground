import numpy as np

ar = np.array([1,2,3])
#add 7 before index 1 of the input array ar
ar1 = np.insert(ar,1,7) 
print(f"ar : {ar}")
print(f"ar1 : {ar1}")

ar = np.array([1,2,3])
#add 7,8,9 before index 1 of the input array ar
ar1 = np.insert(ar,1,[7,8,9]) 
print(f"ar : {ar}")
print(f"ar1 : {ar1}")

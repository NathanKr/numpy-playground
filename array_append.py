import numpy as np

# append scalar
ar = np.array([])
ar = np.append(ar,1) 
ar = np.append(ar,2) 
print(ar)

# append 1D list\array to 1D array
ar = np.array([])
ar = np.append(ar,[1,2,3]) 
ar = np.append(ar,[4,5,6]) 
print(ar)

# append array to 2D array
ar = np.array([[1,2,3]])
ar = np.append(ar,[[4,5,6]]) 
print(ar)

# append array to 2D array
ar = np.array([[1,2,3]])
ar = np.append(ar,[[4,5,6]],axis=0) 
print(ar)

# append array to 2D array
ar = np.array([[1,2,3]])
ar = np.append(ar,[[4,5,6]],axis=1) 
print(ar)

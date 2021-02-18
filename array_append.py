import numpy as np

# append scalar
ar = np.array([])
ar = np.append(ar,1) 
ar = np.append(ar,2) 
print(ar)

# append 1D list\array to 2D array  
ar = np.array([])
ar = np.append(ar,[1,2,3]) 
ar = np.append(ar,[4,5,6]) 
ar = ar.reshape((2,3))
print(ar.shape)
print(ar)

# append 1D array to 2D array , no axis

ar = np.array([[1,2,3]])
ar = np.append(ar,[[4,5,6]]) 
print(ar)

# append 1D array to 2D array , axis=0
ar = np.array([[1,2,3]])
ar = np.append(ar,[[4,5,6]],axis=0) 
print(ar.shape)
print(ar)

# append 1D array to 2D array , axis=1
ar = np.array([[1,2,3]])
ar = np.append(ar,[[4,5,6]],axis=1) 
print(ar)

# append 1D array to 2D array , vstack
ar = np.array([1,2,3])
ar = np.vstack((ar,[4,5,6])) 
print(ar.shape)
print(ar)

# append 1D array , hstack
ar = np.array([1,2,3])
ar = np.hstack((ar,[4,5,6])) 
print(ar.shape)
print(ar)

# append 1D array to 2D array , insert
ar = np.zeros((2,3))
ar[0,:] = [1,2,3]
ar[1,:] = [4,5,6]
print(ar.shape)
print(ar)
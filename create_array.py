import numpy as np

ar_0d = np.array(13)
print ("ar_0d.ndim : ",ar_0d.ndim)
print ("zero dimension array\n",ar_0d)

ar_1d = np.array([1,2,3,4])
print ("ar_1d.ndim : ",ar_1d.ndim)
print ("one dimension array\n",ar_1d)

ar_2d = np.array([[1 , 2 , 3],[3 , 4 , 5]])
print ("ar_2d.ndim : ",ar_2d.ndim)
print ("two dimensions array 2x3\n",ar_2d)

ar_3d = np.array([ar_2d,ar_2d,ar_2d,ar_2d])
print ("ar_3d.ndim : ",ar_3d.ndim)
print ("three dimensions array 2x3x4\n",ar_3d)

array_2d = np.array([3 , 4 , 5], ndmin=2)
print ("array_2d.ndim : ",array_2d.ndim)
print ("two dimensions array created with ndmin \n",array_2d)


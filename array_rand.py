import numpy as np

np.random.seed(42)

# 1D array with 5 random integers range 0-100 (0 is included , 100 is not included)
arr_1d = x=np.random.randint(100, size=(5)) 
print("arr_1d\n",arr_1d)



# 2D array 2x4 with integers range 0-100 (0 is included , 100 is not included)
arr_2d = x=np.random.randint(100, size=(2,4)) 
print("arr_2d\n",arr_2d)

print(np.random.rand(3, 2)) 
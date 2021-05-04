import numpy as np

ar_1d = np.array([1,2,3,4,5,6,7,8])
print("ar_1d\n",ar_1d)

splitted_array1 = np.array_split(ar_1d,4)
print("splitted_array1\n",splitted_array1)
print("splitted_array1[0]\n",splitted_array1[0])
print("splitted_array1[3]\n",splitted_array1[3])





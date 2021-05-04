import numpy as np

arr_1d = np.array([1,3,5,7,9,13,44])
print("arr_1d\n",arr_1d)

start_index=1
last_index=4
#start_index is included but last_index is excluded
print("second ,third and forth items\n",arr_1d[start_index:last_index]) #indexes : 1,2,3 -> values : 3,5,7

print("all items after the second item\n",arr_1d[2:]) # index 2 is included -> 5,7,9,13,44
print("all items before the third item\n",arr_1d[:2]) # index 2 is excluded -> 1,3
print("last 3 items\n",arr_1d[-3:]) #  9,13,44
print("use step 2\n",arr_1d[0::2]) #  index 0 , 2  , 4  , 6 -> 1,5,9,44

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("first two items on last two rows\n",arr_2d[-2:,0:2]) # [4,5] , [7,8]
print("first row\n",arr_2d[0,:]) # [1,2,3]
print("first column\n",arr_2d[:,0]) # [1,4,7]



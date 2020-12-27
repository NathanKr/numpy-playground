import numpy as np

arr_1d = np.array([1,3,5,7])
print("arr_1d\n",arr_1d)
print("first item in the array -> arr_1d[0] : ",arr_1d[0])

arr_2d = np.array([[1,3,5,7],[11,222,33,44]])
print("arr_2d\n",arr_2d)
print("first item in the first row -> arr_1d[0][0] : ",arr_2d[0][0])
print("last item in the first row -> arr_1d[-1][0] : ",arr_2d[-1][0])
print("first item in the second row -> arr_1d[1,0] : ",arr_2d[1,0])
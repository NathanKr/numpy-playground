import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])

result = np.where(arr_1d == 4)
print("result found : ",result)
print("result[0] : ",result[0])

result = np.where(arr_1d == 14)
print("result not found : ",result)
print("result[0] : ",result[0])




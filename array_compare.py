import numpy as np

ar1 = np.array([1,2,3])
ar2 = np.array([4,5,6])
ar3 = np.array([1,2,3])
ar4 = np.array([[1,2,3],[4,5,6]])

# number of items in an array
print(f"number of items in ar4 : {ar4.size}")

# compare array , == compare the data element wise
print(ar1 == ar1)
print(ar1 == ar3)
print(ar1 == ar2)

# compare array
print(np.array_equal(ar1, ar1))
print(np.array_equal(ar1, ar3))
print(np.array_equal(ar1, ar2))
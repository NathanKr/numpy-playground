import numpy as np

def increment(a):
    return a+1

vfunc = np.vectorize(increment)
print(vfunc([1, 2, 3, 4]))

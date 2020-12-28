import numpy as np

ar_2d = np.array([[1 , 2 , 3],[3 , 4 , 5]])
print("ar_2d\n",ar_2d)

print("sum\n",ar_2d.sum())
print("sum(axis=0)\n",ar_2d.sum(axis=0))
print("sum(axis=1)\n",ar_2d.sum(axis=1))
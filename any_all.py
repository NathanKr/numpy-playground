import numpy as np

ar1 = np.array([True, False , True])
ar2 = np.array([True, True , True])
ar3 = np.array([False, False , False])
ar4 = np.array([False, True , False])



print(f"np.all(ar1) : {np.all(ar1)}")
print(f"np.all(ar2) : {np.all(ar2)}")
print(f"np.any(ar3) : {np.any(ar3)}")
print(f"np.any(ar4) : {np.any(ar4)}")
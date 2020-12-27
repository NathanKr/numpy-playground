import numpy as np

grades_1d = np.array([55,88,34,56,100,89])
print("grades before reshape\n",grades_1d)

grades_2d = grades_1d.reshape(2,3)
print("grades after reshape\n",grades_2d)

print("convert grades_2d to 1d array",grades_2d.reshape(-1))



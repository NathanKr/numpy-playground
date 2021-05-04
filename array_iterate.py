import numpy as np

grades_1d = np.array([55,88,34,56,100,89])
print("grades_1d\n",grades_1d)
for grade in grades_1d:
    print (grade)


names_2d = np.array([["Jim" , "John"] , ["Mike" , "Mor"]])
print("grades_2d\n",names_2d)
print("iterate names_2d using two for")
for row in names_2d:
    for name in row:
        print(name)

print("iterate names_2d names using one for")
for name in np.nditer(names_2d):
    print (name)


print("iterate names_2d names using one for and index")
for i,name in enumerate(names_2d):
    print (i,name)

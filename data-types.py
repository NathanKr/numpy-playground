import numpy as np

names = np.array(["Jim" , "John" , "Sara"])
print("names\n",names)
print("names.dtype : ",names.dtype)

salaries = np.array([8000 , 10000 , 20000])
print("salaries\n",salaries)
print("salaries.dtype : ",salaries.dtype)

ages_as_string = np.array([44,66,45],dtype="S") # represent as strings
print("ages_as_string\n",ages_as_string) # why do i get b ???
print("ages_as_string.dtype : ",ages_as_string.dtype)

import numpy as np
# Teta is features vector : teta_0,teta_1,....,teta_n . Teta is column vector (n+1)x1 (n+1 is the number of features)

# X is a matrix [X0,X1,X2,....,Xn]. each X0,X1,X2,....,Xn is a column vector mX1 where m is number of data set points. thus X is m*n. Notice that X0 is always 1

# X*Teta is : teta0*X0 + teta1*X1 + ….. +teta_n*Xn .i.e. X*Teta is a column vector mX1 

# for example suppose we have 3 features i.e. teta0,teta1,teta2
Teta = np.array([2,3,-0.5])
print("Teta : ",Teta)
m=10
# for example suppose we have 10 data set points
X0 = np.ones(m)
print("X0 : ",X0)

X1 = np.arange(0,m,1)
print("X1 : ",X1)

X2 = np.arange(20,m+20,1)
print("X2 : ",X2)

mat = np.vstack((X0,X1,X2)).T
print("mat.shape : ",mat.shape)

# both solutions works
print(np.dot(mat,Teta))
print(np.matmul(mat,Teta))



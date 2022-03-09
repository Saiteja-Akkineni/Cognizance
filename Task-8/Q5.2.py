import numpy as np
row=int(input("Enter no. of rows in the matrix:"))
col=int(input("Enter no. of columns in the matrix"))
rt=np.array([])
x=np.array([])
for i in range(0,row*col):
    num=int(input("Enter the elemets (from 1x1-1x2...):"))
    rt=np.append(rt,num)
x=np.reshape(rt,(row,col))
fac=int(input("Enter the factor by which you like to multiply:"))
for j in range(0,row):
    for k in range(0,col):
        x[j][k]=x[j][k]*fac
for r in range(0,row):
    for k in x[r]:
        print(k,end=" ")
    print(" ")

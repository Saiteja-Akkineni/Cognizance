import numpy as np
a=int(input("Enter the first number:"))
b=int(input("Enter the last number:"))
if a>b:
    print("Error,Last number should be greater than the first")  
else:
    arr=np.array([a])
    zero=np.array([0]*5)
    for i in range(a+1,b+1):
        temp=np.array([i])
        arr=np.concatenate((arr,zero,temp))
    print(arr)
import numpy as np
arr1 = np.array([])
arr2 = np.array([])
le=int(input("Enter the size of both arrays:"))
for i in range(0,le):
    num=int(input("Enter a elemets of 1st array:"))
    arr1=np.append(arr1,num)
for j in range(0,le):
    num=int(input("Enter a elemet of 2nd array:"))
    arr2=np.append(arr2,num)
print ("1st array : ", arr1)  
print ("2nd array : ", arr2)  
sumarr = np.add(arr1, arr2)  
print ("added array : ", sumarr)
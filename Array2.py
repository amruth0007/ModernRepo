import numpy as num
arr1=num.array([10,20,30,40])
arr2=arr1.copy()
arr1[2]=25
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)
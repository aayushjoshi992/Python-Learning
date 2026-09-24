import numpy as np
import pandas as pd

arr=np.array([1,2,3,4,5])
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
arr2=np.arange(24)
print(arr2)
arr3=np.arange(0,10,2)
print(arr3)
print(np.log(arr3))
print(np.sqrt(arr3))
print(np.pow(arr3,2))
print(np.std(arr2))

print(np.ndim(arr2))
print(np.shape(arr2))


A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])
print(np.dot(A,B))
print(A@B)


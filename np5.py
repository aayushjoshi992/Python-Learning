import numpy as np
arr=np.array([10,np.nan,20,np.nan,40,50])
# print(arr)
print(np.isnan(arr))
print(np.isnan(arr).sum())

arr[(np.isnan(arr))]=0
print(arr)

#Replacing Missing values with Mean
import numpy as np
arr=np.array([10,np.nan,20,np.nan,40,50])
# print(arr)
print(np.isnan(arr))
print(np.isnan(arr).sum())

# arr[(np.isnan(arr))]=0
# print(arr)

#Replacing Missing values with Mean
mean_val=np.nanmean(arr)
print(mean_val)
arr[np.isnan(arr)]=mean_val
print(arr)

#Replace missing values with Meadian
arr=np.array([10,20,np.nan,40])
median=np.nanmedian(arr)
print(median)
arr[np.isnan(arr)]=median
print(arr)

#Replace mIssing values with custom value
arr=np.array([5,np.nan,15])
arr=np.nan_to_num(arr,nan=1)
print(arr)

#below functions for aggregate value in NaN
print(np.nansum(arr))
print(np.nanmax(arr))
print(np.nanmin(arr))
print(np.nanstd(arr))

#missing value in 2D array
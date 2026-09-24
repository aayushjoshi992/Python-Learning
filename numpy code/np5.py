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
print('missing value in 2D array')
arr=np.array([[1,2,np.nan],[4,np.nan,6]])
print(np.nanmean(arr))#find mean
print(np.nansum(arr))#find sum

#filling missing value with 1 
arr= np .array([2,np.nan,4])
arr[(np.isnan(arr))]=1
print(arr)

#row wise sum in 2D array
arr=np.array([[1,2,np.nan],[4,np.nan,6]])
print(np.nansum(arr,axis=0)) #row wise sum
print(np.nansum(arr,axis=1)) #col wise sum



sales=np.array([1000,2000,1500,3000])
growth_factor=np.array([1.1,np.nan,0.95,np.nan])
#here filling growth factor by 1
growth_factor=np.nan_to_num(growth_factor, nan=1)
print(growth_factor)
#and multiplying to sales array to adjust the value
#we have increased the sales value by growth factor
adjusted_sales=sales*growth_factor
#see the difference in output below
print(sales)
print(adjusted_sales)


# Mathematical and Statistical Operation in Numpy
import numpy as np

# #Basic Mathematical Operations
arr= np.array([10,20,30,40,50])
print(arr)
print(np.add(arr,10))
print(np.subtract(arr,5))
print(np.multiply(arr,2))
print(np.divide(arr,2).astype(int))
print(np.pow(arr,2))
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))
arr=np.array([-2,3,-4,25])
print(np.abs(arr))
val=3.333333333
print(f" The value is {val:.2f}")
prices=np.array([10.40,20.60,31.90,55.20])
print(np.round(prices).astype(int))
angles=np.array([0,np.pi/2,np.pi])
angles=np.array([0,90,180,270,360])
print(angles)
print(f"sin functio:{np.sin(angles)}")
print(f"cos func: {np.cos(angles)}")
print(f"tan func: {np.tan(angles)}")

# # Statistical operation
print(np.std(arr))
print(np.var(arr))
print(np.max(arr))
print(np.min(arr))

# Finding max and min value index from an array
arr=np.array([25,15,60,35])
print(np.argmax(arr))
print(np.argmin(arr))
arr=np.array([1,10,100])
print(np.log(arr))
print(np.log10(arr))
print(np.log2(arr).astype(int)) 


arr=np.array([2.3456, 5.6789])
print(np.ceil(arr))
print(np.floor(arr))



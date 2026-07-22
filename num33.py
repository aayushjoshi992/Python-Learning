# #Broadcasting
# # Broadcasting is NumPy’s mechanism for performing arithmetic operations on arrays with different shapes. It stretches the smaller array across the larger array so they have compatible shapes, performing element-wise operations without making unnecessary copies of data in memory.
# #it is a property than an operation done to it
# # vectorization allows us to perform operations on entire arrays without using explicit loops 

import numpy as np

# arr=np.array([1,2,3,4,5])
# res=arr+10
# #here it creates a virtual array of 4 10s and it is then added internally/ It is created in runtime
# # print(res)
# # print(arr*5)
# arr_copy=arr.copy()
# arr_copy+=5
# # print(arr_copy)

# #row vector broadcasting

# a=np.array([
#     [10,20,30,40],
#     [50,60,70,80]
# ])

# b=np.array([2,4,6,8])
# # print(a+b)

# c=np.array([
#     [100],
#     [200]
#     ])
# # print(a+c)
# # vectorization

# a1=np.array([1,2,3,4,5])
# result=[]
# for x in a1:
#     result.append(x*3)
# print(result)

# print(a1*3)

a=np.array([10,20,30,40])
# print(a>25)
# print(a==20)
# print((a>15)&(a<35))
# print("hello world")
# res=np.where(a>25,'High','Low')
# print(res)
print(np.sum(a))
print(np.max(a))
print(np.min(a))
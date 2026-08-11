#Broadcasting is not a it is mechanism that numpy uses to

# Broadcasting="How NumPy makes array shapes compatible" 
# Vectorization="How the operations is performed"
import numpy as np
arr =np.array([1,2,3,4])
# res =arr+10
# print(res)

# [1 2 3 4]
# +
# [10 10 10 10]
# a=np.array([[1,2,3],
#             [4,5,6]])
# b=np.array([10,20,30])


# b=np.array([[100],[200]])
# print(a+b)
a=np.array([1,2,3,4,5])
result=[]
for i in a:
    result.append(i*3)
# print(result)
res=a*3
# print(res)
a=np.array([10,20,30,40])
# print(a>25)
# print((a>15) & (a<35))
a=np.array([10,20,30,40])
result=np.where(a>25,'High','Low')
print(result)

# print(np.max(a))
# print(np.min(a))
# print(np.sum(a))
# print(np.sqrt(a))
# print(np.exp(a))
# print(np.log(a))
arr=np.array([1,2,3,4])
print(arr!=3)
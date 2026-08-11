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
a=np.array([[1,2,3],
            [4,5,6]])
# b=np.array([10,20,30])


b=np.array([[100],[200]])
print(a+b)
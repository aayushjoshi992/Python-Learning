# Numpy
# Numerical computation use garna

import numpy as np
ar=np.array([1,2,3,4,5])
print(ar)
print(type(ar))
print(ar.ndim)
print(ar[3])
print(len(ar))
for a in ar:
    print(a)

arr=np.array([[1,2,3],[4,5,6]])
print(arr)

print(arr.ndim)

# We can also make Array using the range function

arr=np.arange(0,10,2)
print(arr)

print(arr.shape)
print(arr.shape)

a=np.array([10,20,30])
b=np.array([1,2,3])
print(a+b)
print(a-b)

print(a+5)

print(a*2)#broadcasting
print(np.sqrt(a))
print(np.exp(a))
print(np.square(a))
print(np.log(a))
add=np.sum(a)
maximum=np.max(a)
minimum=np.min(a)

print(add)
print(maximum)
print(minimum)

m=np.mean(a)
print(m)


print(np.std(a))


a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

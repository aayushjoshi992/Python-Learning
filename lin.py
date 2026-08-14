#linear algebra is the branch of mathematics that deals with vectors, matrices
#and of linear equations
#Simple definition: Linear algebra is the mathematics of working with of numbers
#(vectors and matrices) to solve equations and model relationships variables


#Dot product gives us one value where as matrix multipications give matrix or vectors
#a scalar is  a single value
#vector is an array whether 1-D or 2-D
import numpy as np
#1. Scalars: A scalar is a single number
# a=5
# b=-4

#vector= np.array([2,4,6])
a=np.array([1,2,3])
b=np.array([4,5,6])
v=np.dot(a,b) #1*4+2*5+6*3
print(v)

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]]) #row multiplies column
#(1*5)+(2*7)=5+14=19
#(1*6)+(2*8)=6+16=22
#(3*5)+(4*7)=15+28=43
#(3*6)+(4*8)=18+32=50
dp=np.dot(A,B)
print(dp)



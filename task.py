import numpy as np
a = np.array([2,3,4,5,6,8,10])
m=np.max(a)
print("Max ",m)
mi=np.min(a)
print("Min ",mi)
print("length ",len(a))

for i in a:
    if(i%2==0):
        print(i) 
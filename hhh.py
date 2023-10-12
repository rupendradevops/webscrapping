import numpy as np
a=np.array([[1,2,3],[0,0,0]])
dim=int(input("enter the dimention:"))
b=np.identity(dim,dtype=int)
print(b,"\n")
print("shape of identical matrix:",b.shape)
print("dimension od identical matrix:",b.ndim)
c=a*dim
print(c,"\n")
d=np.ones_like(c)
print(d)
e=np.zeros_like(c)
print(e)




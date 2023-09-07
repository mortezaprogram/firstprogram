import numpy as np
from scipy.linalg import lu
a=np.mat("1,1,1;3,4,6;2,5,4")
[p,l,u]=lu(a)
print("p: ",p)
print("l: ",l)
print("u: ",u)

r = p.dot(l).dot(u)
print("r = ", r)
m = np.mat(p)*np.mat(l)*np.mat(u)
print("m = ", m)

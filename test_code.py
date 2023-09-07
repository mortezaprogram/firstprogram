import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,4*np.pi,100)
sinx=np.sin(x)
plt.plot(x,sinx)
plt.xlabel("Time")
plt.ylabel("AMP")
plt.title("Sin wave")
plt.xlim(0,4*np.pi)
plt.ylim(-1.5,1.5)
# plt.show()
# y=np.array([[np.arange(1,10)],[np.arange(11,16)]])
c=np.array([[np.arange(1,10)],[np.arange(11, 16)]])
print(c)
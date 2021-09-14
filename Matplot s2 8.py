#Multi Graph 
from matplotlib import pyplot as plt

x1 = [1,3,5,7,9]
x2 = [2,4,6,8,10]

y1 = [10,20,30,40,50]
y2 = [5,10,15,20,25]

plt.subplot(221)

plt.plot(x1,y2)

plt.subplot(222)
plt.plot(x2,y2)

plt.show()

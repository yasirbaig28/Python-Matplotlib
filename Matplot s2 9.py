#Multi Graph 
from matplotlib import pyplot as plt

x1 = [1,2,3,4,5 ]
x2 = [2,4,6,8,10]

y1 = [10,20,30,40,50]
y2 = [5,10,15,20,25]

plt.subplot(221)#221-Means 2-Rows,2-Column,1st-Position
plt.plot(x1,y2,label="x1 vs y1",c='r',linewidth=2)
plt.grid()
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.subplot(224)
plt.plot(x2,y2,label="x2 vs y2",c='b',linewidth=4)
plt.grid()
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

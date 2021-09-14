#Mutiple Graphs with Legends
from matplotlib import pyplot as plt
from matplotlib import style 

style.use('ggplot')
    
x1=[1,2,3,4,5]

y1=[5,10,15,20,45]

x2=[1,3,5,7,9]

y2=[2,4,6,8,10]

plt.plot(x1,y1,c='b',label="x1 vs y1")
plt.plot(x2,y2,c='r',label="x2 vs y2")

plt.title("Multiple Graphs")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()

plt.show()

#colour to graph
from matplotlib import pyplot as plt

x=[1,2,3,4,5]

y=[5,10,15,20,45]

plt.scatter(x,y,c='r')
plt.title("Age vs Marks")
plt.ylabel("age")
plt.xlabel("marks")

plt.show()

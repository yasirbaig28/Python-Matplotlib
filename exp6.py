#Change marker
from matplotlib import pyplot as plt

x=[1,2,3,4,5]

y=[5,10,15,20,45]

plt.scatter(x,y,c='r',s=50,marker="^")
plt.title("Age vs Marks")
plt.ylabel("age")
plt.xlabel("marks")

plt.show()

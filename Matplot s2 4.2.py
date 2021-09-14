#Vertical & Horizontal Bar Graph
from matplotlib import pyplot as plt

plt.barh([1,3,5,7,9],[50,40,70,80,20],label="BMW",color='b',height=0.5)

plt.barh([2,4,6,8,10],[80,20,50,20,60],label="AUDI",color='r',height=0.8)

plt.legend()
plt.title("Cars Sales Data")
plt.xlabel("No of Years")
plt.ylabel("No of Cars sold")
plt.show()

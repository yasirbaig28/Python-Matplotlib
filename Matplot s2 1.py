from matplotlib import pyplot as plt

plt.bar([1,2,3,4,5],[50,40,70,80,20],label="BMW",color='b',width=0.6)

plt.bar([6,7,8,9,10],[80,20,50,20,60],label="AUDI",color='r',width=0.2)

plt.legend()
plt.title("Cars Sales Data")
plt.xlabel("No of Years")
plt.ylabel("No of Cars sold")
plt.show()

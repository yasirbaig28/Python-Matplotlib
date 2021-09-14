from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[50,40,70,80,20],label="BMW",color='b',width=0.5)

plt.bar([2,4,6,8,10],[80,20,50,20,60],label="AUDI",color='r',width=0.5)

plt.legend()
plt.title("Cars Sales Data")
plt.xlabel("No of Years")
plt.ylabel("No of Cars sold")
plt.show()

#Histogram
from matplotlib import pyplot as plt

population = [20,27,28,22,20,27,65,65,43,13,55,33,22,49]#random ages

age_range = [0,10,20,30,40,50,100]#how much we are dividing our histogram into

plt.hist(population,age_range,histtype='bar',rwidth=0.8)
plt.xlabel("Age Group")
plt.ylabel("Number of people")
plt.title("Histogram")

plt.show()

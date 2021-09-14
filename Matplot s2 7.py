#PIE Chart
from matplotlib import pyplot as plt

activities = ['sleeping','eating','classes','social media']

duration = [7,3,12,2]

colors = ['b','g','r','y']

plt.pie(duration,labels=activities,colors=colors,shadow=True,autopct="%1.1f%%",explode=(0.1,0.2,0.3,0.1))

#shadow for 3D effect and autopct to mention percentage in graph
#1.1f for only 1.1 decimal points to be seen in graph
#explode is used to move the part of pie-chart away, it is in tuple

plt.title("My Activities")
plt.show()

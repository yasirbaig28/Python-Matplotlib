from matplotlib import pyplot as plt
from matplotlib import style

import pandas as pd

style.use('ggplot')

data = pd.read_csv('Latest Covid-19 India Status.csv')

x1 = data['Active Ratio (%)']

y1 = data['Death Ratio (%)']

x2 = data['Deaths']

y2 = data['Discharge Ratio (%)']

plt.plot(x1,y1,label="x1 vs y1",c='b',marker="*")

plt.plot(x2,y2,label="x2 vs y2",c='r',marker="^")

plt.title("Latest Covid-19 India Status")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True,color='y')
plt.show()

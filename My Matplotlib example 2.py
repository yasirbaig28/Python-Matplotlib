from matplotlib import pyplot as plt
from matplotlib import style

import pandas as pd

style.use('ggplot')

data = pd.read_csv('vaccination-data(26-08-2021).csv')

x1 = data['PERSONS_VACCINATED_1PLUS_DOSE']

y1 = data['PERSONS_VACCINATED_1PLUS_DOSE_PER100']

x2 = data['PERSONS_FULLY_VACCINATED']

y2 = data['PERSONS_FULLY_VACCINATED_PER100']

plt.scatter(x1,y1,label="x1 vs y1",c='b',marker="*")

plt.scatter(x2,y2,label="x2 vs y2",c='r',marker="^")

plt.title("Vaccination Data of Aug 2021")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True,color='y')
plt.show()

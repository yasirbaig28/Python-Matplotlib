#MATPLOT WITH PANDAS FOR REAL-LIFE DATASET

from matplotlib import pyplot as plt
from matplotlib import style

import pandas as pd

style.use('ggplot')

data = pd.read_csv('diabetes.csv')

x = data['BMI']

y = data['Outcome']

plt.scatter(y,x,label="x vs y",c='b',s=50,marker=".",linewidth=2    )

plt.title("Diabetes")
plt.xlabel("GLUCOSE")
plt.ylabel("OUTCOME")
plt.legend()
plt.grid(True,color='y')
plt.show()


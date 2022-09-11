import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import seaborn as sns
from IPython.display import display
import sklearn
from sklearn import *
from sklearn.preprocessing import FunctionTransformer

# sample from linear regression
x = np.linspace(0, 30, num=100)
delta = np.random.uniform(-2, 2, size=(len(x),))
lin = -.4*x + 27
y = lin + delta

# Plot data
plt.scatter(x, y, c="b")
plt.plot(x,lin, 'r-')
plt.xlabel('Windgeschwindigkeit in Knoten')
plt.ylabel('Gefühlte Temperatur (C)')
plt.show()
# plt.savefig('img/toy_data_plot_lin.png')

d = {'Wind (knots)': x, 'Gefühlte Temperatur (C)': y}
df = pd.DataFrame(data=d)
df.to_csv('data/toyData_wind.csv', index=False)

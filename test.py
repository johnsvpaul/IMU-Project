from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv',sep=r'\s*,\s*')

data['Time'] = pd.to_datetime(data['Time'])


time =  data['Time']
magx = data['MagX']
accx = data['AccY']

plt.plot_date(time, accx, linestyle='solid')
plt.show()

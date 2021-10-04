import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv',sep=r'\s*,\s*')
data.to_csv('dfsavename.csv.gz', compression='gzip')
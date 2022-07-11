import pandas as pd
import csv
import plotly.figure_factory as ff
data=pd.read_csv('data.csv')
fig=ff.create_distplot([data['Avg Rating'].tolist()],['Avg Rating'])
fig.show()
import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("project-107.csv")

fig=ff.create_distplot([df["Avg"].tolist()],["Brand"],show_hist=False)
fig.show()
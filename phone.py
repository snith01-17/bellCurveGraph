import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("data5.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile"], show_hist=False)
fig.show()
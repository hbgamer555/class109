import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv(  r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\data10.csv")
Height1=df["Height"]
x1=statistics.mean(Height1)
print(x1)
y1=statistics.median(Height1)
print(y1)
z1=statistics.mode(Height1)
print(z1)

fig=ff.create_distplot([df["Height"].tolist()],["Height"],show_hist=False)
fig.add_trace(go.Scatter(x=[y1, y1], y=[0, 0.2], mode="lines", name="MEDIAN"))
fig.add_trace(go.Scatter(x=[x1,x1],y=[0,0.2],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[z1,z1],y=[0,0.2],mode="lines",name="MODE"))
fig.show()



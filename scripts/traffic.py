'''
import plotly.plotly as py
from plotly.graph_objs import *

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 7, 9]
)
data = Data([trace0, trace1])

py.plot(data, filename='basic-line', fileopt='overwrite', auto_open=False)
'''

# offline plot
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

fig = py.get_figure('https://plot.ly/~cftang/23', raw=True)
plot(fig, auto_open=False)

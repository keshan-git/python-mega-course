from bokeh.plotting import figure
from bokeh.io import output_file, show

import pandas as pd


x = [1, 2, 3, 4]
y = [6, 7, 8, 9]

output_file('graphs/line.html')

fig = figure(plot_width=400, plot_height=400, title=None, toolbar_location="below")
fig.line(x, y)
fig.circle(x, y, size=10)

show(fig)

output_file('graphs/bachelors.html')
df = pd.read_csv('http://pythonhow.com/data/bachelors.csv')

fig = figure(plot_width=800, plot_height=600, title=None, toolbar_location="below")
fig.line(df['Year'], df['Engineering'])
fig.circle(df['Year'], df['Engineering'], size=10)

# show(fig)

fig = figure(plot_width=500, plot_height=400, tools='pan')

fig.title.text = "Cool Data"
fig.title.text_color = "Gray"
fig.title.text_font = "times"
fig.title.text_font_style = "bold"
fig.xaxis.minor_tick_line_color = None
fig.yaxis.minor_tick_line_color = None
fig.xaxis.axis_label = "Year"
fig.yaxis.axis_label = "Engineering"

fig.line(df['Year'], df['Engineering'])
show(fig)

output_file('graphs/weather.html')
weather = pd.read_excel('http://pythonhow.com/data/verlegenhuken.xlsx')
fig = figure(plot_width=500, plot_height=500, title='Temperature Vs Pressure', toolbar_location="below")
fig.xaxis.axis_label = "Temperature (C)"
fig.yaxis.axis_label = "Pressure (hPa)"

fig.circle(weather['Temperature'] / 10, weather['Pressure'] / 10, size=0.5)

show(fig)


time_series_data = pd.read_csv('time_series_data.csv', parse_dates=['Date'])

fig = figure(plot_width=800, plot_height=400, x_axis_type='datetime', title='Time Series', toolbar_location="below")
fig.line(time_series_data['Date'], time_series_data['Close'], color='orange', alpha=0.8)

output_file('graphs/time_series.html')
show(fig)
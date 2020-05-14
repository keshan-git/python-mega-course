from math import pi
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN


def generate():
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()

    data_source = data.DataReader(name='AAPL', data_source='yahoo', start=start, end=end)

    data_inc = data_source.Close > data_source.Open
    data_dec = data_source.Open > data_source.Close
    half_day = 12 * 60 * 60 * 1000  # half day in ms

    graph = figure(x_axis_type='datetime', width=800, height=300)
    graph.xaxis.major_label_orientation = pi / 4
    graph.grid.grid_line_alpha = 0.3

    graph.segment(data_source.index, data_source.High, data_source.index, data_source.Low, color='black')
    graph.vbar(data_source.index[data_inc], half_day, data_source.Open[data_inc], data_source.Close[data_inc],
               fill_color='#D5E1DD', line_color='black')
    graph.vbar(data_source.index[data_dec], half_day, data_source.Open[data_dec], data_source.Close[data_dec],
               fill_color='#F2583E', line_color='black')

    # output_file('candlestick.html', title='Candlestick Chart')
    # show(graph)

    js_code, div_comp = components(graph)
    js_file_paths = CDN.js_files
    css_file_paths = CDN.css_files

    return js_code, div_comp, js_file_paths, css_file_paths

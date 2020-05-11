from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import Range1d, HoverTool, ColumnDataSource
import pandas as pd


class MotionGraph:
    def __init__(self):
        self.graph = figure(plot_height=50, x_axis_type='datetime', title='Motion Detection', toolbar_location="below")
        self.graph.yaxis.visible = False
        self.graph.sizing_mode = 'scale_width'
        self.graph.y_range = Range1d(0, 1)
        self.graph.ygrid[0].ticker.desired_num_ticks = 1

        hover = HoverTool(tooltips=[('Start ', '@Start_str'), ('End ', '@End_str')])
        self.graph.add_tools(hover)

        output_file('detection.html')

    def show(self):
        data_set = pd.read_csv('detection.csv', parse_dates=['Start', 'End'])
        data_set['Start_str'] = data_set['Start'].dt.strftime('%y-%m-%d %H:%M:%S')
        data_set['End_str'] = data_set['End'].dt.strftime('%y-%m-%d %H:%M:%S')
        column_data_source = ColumnDataSource(data_set)

        self.graph.quad(top=1, bottom=0, left='Start', right='End', source=column_data_source, color="orange")

        show(self.graph)

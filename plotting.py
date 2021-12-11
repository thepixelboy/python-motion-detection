from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, output_file, show

from motion_detection import df

# convert datetime values from df to strings
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# create a ColumnDataSource
cds = ColumnDataSource(df)

# create figure object
p = figure(x_axis_type="datetime", width=500, height=100, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

# create a hover object
hover = HoverTool(
    tooltips=[
        ("Start", "@Start_string"),
        ("End", "@End_string"),
    ]
)

p.add_tools(hover)

# create a quadrant
q = p.quad(
    left="Start",
    right="End",
    bottom=0,
    top=1,
    color="green",
    source=cds,
)

# output file
output_file("motion_graph.html")

# write the plot in the figure object
show(p)

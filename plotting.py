from bokeh.plotting import figure, output_file, show

from motion_detection import df

# create figure object
p = figure(x_axis_type="datetime", width=500, height=100, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

# create a quadrant
q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

# output file
output_file("motion_graph.html")

# write the plot in the figure object
show(p)

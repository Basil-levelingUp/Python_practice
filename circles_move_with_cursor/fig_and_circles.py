import bokeh.plotting as bk

# output to static HTML file
bk.output_file("out.html")

# Create window
fig = bk.figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
fig.circle([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], size=20, color="navy", alpha=0.5)

# Show output figure
bk.show(fig)

stopgap = 1
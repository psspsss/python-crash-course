from matplotlib.pyplot
import pygal
from pygal.style import DarkStyle
from random_walk import RandomWalk

while True:
    rw = RandomWalk(1000)

    rw.fill_walk()

    points = list(zip(rw.x_values, rw.y_values))

    chart = pygal.XY(
        title="Random Walk (XY scatter)",
        style=DarkStyle,
        x_title="X",
        y_title="Y",
        show_legend=False,
        show_x_guides=False,
        show_y_guides=False,
        dots_size=1,
    )

    chart.add("walk", points)
    chart.render_to_file("random_walk_pygal.svg")
    keep_running = input("Make another walk? y/n : ")
    if keep_running == "n":
        break
# plt.savefig(".png")

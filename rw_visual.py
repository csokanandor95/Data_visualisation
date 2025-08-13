import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making random walks as long as the program is active

while True:

    # make a random walk

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9), dpi=128) # set to screen size
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.set_aspect('equal') # both axes have equal spacing between tick marks

    # emphasize the first and last points

    ax.scatter(0, 0, c='green', edgecolors='none', s=100) # starting point in green
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) # ending point in green

    # remove axes

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
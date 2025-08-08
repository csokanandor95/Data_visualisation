import matplotlib.pyplot as plt # pyplot module contains functions that help generate charts and plots

squares = [1,4,9,16,25]

# fig is the entire figure
# ax is a single plot in the figure - used mostly for customizing

fig, ax = plt.subplots() # this function generates plots in the same figure
ax.plot(squares) # plot method tries to plot the data given

plt.show() # opens Matplotlib's viewer and displays the plot
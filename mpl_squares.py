import matplotlib.pyplot as plt # pyplot module contains functions that help generate charts and plots

squares = [1,4,9,16,25]

# fig is the entire figure
# ax is a single plot in the figure - used mostly for customizing
fig, ax = plt.subplots() # this function generates plots in the same figure
ax.plot(squares, linewidth=3) # plot method tries to plot the data given

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels
ax.tick_params(labelsize=14)

plt.show() # opens Matplotlib's viewer and displays the plot
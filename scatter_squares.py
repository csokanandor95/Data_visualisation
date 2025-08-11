import matplotlib.pyplot as plt

# to plot a single pont, pass the x and y values

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

# plot or style individual points by scatter() = pontdiagram
#ax.scatter(2,4,s=200) # s = size of data point

# plotting series of points with scatter()
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# adding colormap instead of a color or rgb code
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(labelsize=14)

#set the range for each axis
ax.axis([0, 1100, 0, 1_000_000])
ax.ticklabel_format(style='plain') # can be other e.g. scientific (default)

# can also save plots and delet extra whitespace with bbox_inches='tight'
plt.savefig('squares_plt.png')
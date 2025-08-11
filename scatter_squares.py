import matplotlib.pyplot as plt

# to plot a single pont, pass the x and y values

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

# plot or style individual point by scatter()
ax.scatter(2,4,s=200) # s = size of data point

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(labelsize=14)

plt.show()
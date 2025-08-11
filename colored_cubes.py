import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes", fontsize=14)

ax.tick_params(labelsize=14)

ax.ticklabel_format(style='scientific')

plt.show()
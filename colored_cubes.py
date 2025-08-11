import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]

ax.scatter(x_values, y_values, s=100)

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes", fontsize=14)

plt.show()
import matplotlib.pyplot as plt


# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)


# =============================================================================

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')




# =============================================================================


# =============================================================================

# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# # Set chart title, and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# plt.tick_params(axis='both', which='major', labelsize=14)

# # Set the range for each axis.
# plt.axis([0, 1100, 0, 1100000])

# plt.show()

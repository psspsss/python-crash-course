import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

plt.title("Scatter Square", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squared", fontsize=14)

# x_vals = [1, 2, 3, 4, 5]
# y_vals = [1, 4, 6, 16, 25]

x_vals = list(range(1, 1001))
y_vals = [x**2 for x in x_vals]
# plt.scatter(x_vals, y_vals, c=(0, 0, 1), edgecolor="none", s=40)

plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, edgecolor="none", s=40)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis="both", which="major", labelsize=14)

plt.savefig("sqaures_plot.png", bbox_inches="tight")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8")
plt.title("Cubes", fontsize=20)
plt.xlabel("Number", fontsize=10)
plt.ylabel("Cubed", fontsize=10)

# plt.plot(x_values, y_values, c="red")
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=20)
plt.axis([0, 5100, 0, 125000000000])


plt.savefig("cubes.png", bbox_inches="tight")
plt.show()

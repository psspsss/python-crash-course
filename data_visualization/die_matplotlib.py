import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()

die_1_results = []
die_2_results = []
results = []
for num in range(1000):
    die1_rolls = die_1.roll()
    die2_rolls = die_2.roll()
    res = die1_rolls + die2_rolls
    results.append(res)

    die_1_results.append(die1_rolls)
    die_2_results.append(die2_rolls)

plt.scatter(die_1_results, die_2_results, c=results, cmap=plt.cm.Purples, s=5)
plt.title("Scatter Output of Two D6 dices")
plt.xlabel("Die 1 output")
plt.ylabel("Die 2 output")
plt.savefig("2d6_scatter.svg")
plt.show()


# frequencies = []
# max_res = die_1.num_sides * die_2.num_sides
# for value in range(2, max_res + 1):
#     freq = results.count(value)
#     frequencies.append(freq)

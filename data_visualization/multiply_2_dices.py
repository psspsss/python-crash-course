import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_res = die_1.num_sides * die_2.num_sides
for value in range(2, max_res + 1):
    freq = results.count(value)
    frequencies.append(freq)

hist = pygal.Bar()

hist.title = "2 D6 dice rolled and multiplied 1000 times"
hist.x_labels = [num for num in range(2, max_res + 1)]
hist.x_title = "Freq of Results"

hist.add("D6 * D6", frequencies)
hist.render_to_file("two_d6_multi.svg")

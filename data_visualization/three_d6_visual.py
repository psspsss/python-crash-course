import pygal

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

results = []

for num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

frequencies = []

max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result + 1):
    freq = results.count(value)
    frequencies.append(freq)

hist = pygal.Bar()

hist.title = "3 D6 dice rolled 1000 times"
hist.x_labels = [num for num in range(0, max_result + 1)]
hist.x_title = "Freq of result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("3_D6_dices.svg")

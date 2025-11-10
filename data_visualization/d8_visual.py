import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []


for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_res = die_1.num_sides + die_2.num_sides
for value in range(2, max_res + 1):
    freq = results.count(value)
    frequencies.append(freq)

hist = pygal.Bar()

hist.title = "Two D8 dices rolled 1000 times"
hist.x_labels = [num for num in range(2, max_res + 1)]
hist.x_title = "Freq of result"

hist.add("D8 + D8", frequencies)
hist.render_to_file("d8_visual.svg")

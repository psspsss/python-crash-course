import pygal
from die import Die


die1 = Die()
die2 = Die()

results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)


frequencies = []
max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result + 1):
    freq = results.count(value)
    frequencies.append(freq)


hist = pygal.Bar()

hist.title = "Results of rolling Two D6 dice 1000 times."
hist.x_labels = [num for num in range(2, max_result + 1)]
hist.x_title = "Result"
hist.x_title = "Frequency of Result"


hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")

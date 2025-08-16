import plotly.express as px

from die import Die

# create a D6 object
die = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyze the results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualise the results
title = "Results of rolling one D6 1000 times"
labels = {'x': 'Result', 'y': 'Frequncy of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) # could be: px.scatter, px.line etc.
fig.show() # dynamic and interactive HTML chart
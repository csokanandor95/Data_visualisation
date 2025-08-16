import plotly.express as px

from die import Die

# create 2 D6 object
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualise the results
title = "Results of rolling 2 D6 dice 1000 times"
labels = {'x': 'Result', 'y': 'Frequncy of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) # could be: px.scatter, px.line etc.

# further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show() # dynamic and interactive HTML chart

fig.write_html('dice_visual_d6d10.html') # must provide file name
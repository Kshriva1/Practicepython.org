import json
from bokeh.plotting import figure, show, output_file
from collections import Counter
month = []
birthday = dict()


with open('birthday.json','r') as w:
    birthday = json.load(w)
for x in birthday.values():
    month.append(x.split('/')[1])
print(Counter(month))
output_file('plot.html')
x_categories = list(birthday.keys())
x = list(birthday.keys())
y = list(birthday.values())
p = figure()
p = figure(x_range = x_categories)
p.vbar(x=x, top = y, width = 0.5)
show(p)



w

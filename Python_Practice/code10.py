import random

a = random.sample(range(0,9),7)
b = random.sample(range(0,9),6)

c = list(set([x for x in a for y in b if x==y]))

print(c)

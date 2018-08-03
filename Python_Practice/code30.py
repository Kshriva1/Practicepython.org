import random
with open("sowpods.txt",'r') as f:
    lst = f.readlines()
print(random.choice(lst).strip())

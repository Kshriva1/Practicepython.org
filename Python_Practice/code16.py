import random
import re

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)

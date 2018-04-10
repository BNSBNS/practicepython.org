import random

a = random.sample(range(0,20), 10)
b = random.sample(range(0,20), 15)

c = [i for i in a if i in b]

print (c)
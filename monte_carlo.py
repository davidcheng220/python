import random

# run 10000 time
total = 100000000000

i = 0
# count the cordinate is in the circle
count = 0

while i < total:
    # x, y in random location
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    # if the cordinate is in the circle count + 1
    if x**2 + y**2 <= 1:
        count += 1
    # total times
    i = i + 1

ratio = count / total

print(ratio*4)

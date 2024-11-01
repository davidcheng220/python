# win propability
# win = (n-1)/n * 1/(n-2)

# def win(n):
#     return (n-1)/n * 1/(n-2)

import random

# n doors
n = 3
win, lose = 0, 0
total = 1000000

for i in range(total):
    doors = [0] * (n - 1)
    idx = random.randint(0, len(doors)-1)
    doors.insert(random.randint(0, len(doors)-1), 1)
    # print(doors)
    # 0 = lose, 1 = win
    # choose random door (x)
    idx = random.randint(0, len(doors) - 1)
    # print("choose this door", doors[idx])

    doors.pop(idx)
    # print("rest door", doors)
    # host opens one of the door that is nothing behind the door (x)
    doors.remove(0)
    # print("doors left: ", doors)
    # deduct these two options, choose another door
    idx = random.randint(0, len(doors)-1)


    if doors[idx] == 1:
        # print("win")
        win += 1
    else:
        # print("lose")
        lose += 1

ratio = win/total

print(ratio)
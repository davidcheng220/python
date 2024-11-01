import random

win, lose = 0, 0

# while win < 3 and lose < 3:
#     # win = 1 | even = 0 | lose = -1
#     score = random.randint(-1,1)
#     print(score)
#     if score == -1:
#         lose += 1
#     elif score == 1:
#         win += 1

# if win == 3:
#     print("win")
# if lose == 3:
#     print("lose")

while True:
    # win = 1 | even = 0 | lose = -1
    score = random.randint(-1,1)
    print(score)
    if score == -1:
        lose += 1
    elif score == 1:
        win += 1
    
    if win == 3:
        print("Win")
        break
    elif lose == 3:
        print("Lose")
        break


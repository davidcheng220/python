import random

low, high = 1, 100
ans = random.randint(low + 1, high -1)
count = 0
while True:
    print("please input", low, ' - ', high, ": ")
    guess = int(input())
    if guess < high and guess > low:
        if guess > ans:
            print("too big")
            high = guess
            count += 1
        elif guess < ans:
            print("too small")
            low = guess
            count += 1
        else:
            print("Correct!")
            print("Total guess: ", count)
            break
    else:
        print("invalid")
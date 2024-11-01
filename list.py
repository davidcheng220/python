# list用在for loop要加range跟len

score = [80, 60, 90, 20, 100]
count = 0

for index in range(len(score)):
    if score[index] >= 60:
        count += 1
print(count)


# for i in score:
#     if i >= 60:
#         count += 1
# print(count)

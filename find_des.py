
# 3 / 5
a, b = 3, 5
ans = "0."
i = 0

while True:
    # 3*10
    a10 = a*10
    ans = ans + str(a10//b)
    print(ans) 
    # 30%5
    a = a10 % b
    if a == 0:
        break

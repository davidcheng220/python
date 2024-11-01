# print a triangle
# *
# **
# ***

row = int(input("input how many rows that you want to make for a triangle: "))
# using for loop and print it by *
for i in range(row + 1):
    print(i*"*")

# inverse triange
# *****
#  ****
#   ***
#    **
#     *
# solution: i is white spaces and row - i is the rest that will be printed by *
for i in range(row + 1):
    print(i * " " + "*" * (row - i))

# print prymid
#     *     1 = 4 * " "  + 1 * "*" 
#    ***    3 = 3 * " "  + 2 * "*"  
#   *****   5 = 2 * " "  + 3 * "*" 
#  *******  7 = 1 * " "  + 4 * "*" 
# ********* 9 = 0 * " "  + 5 * "*" 
left = " "
star_mark = "*"
for i in range(row + 1):
    left_white = row - i
    middle = i * 2 - 1 
    print(left * left_white + middle * star_mark)

# inverse prymid
# *********
#  *******
#   *****
#    ***
#     *
# middle*
# * = row - i * 2 - 1
# 9 = 5 * 2 - 1
# 7 = 4 * 2 - 1
# 5 = 3 * 2 - 1
# 3 = 2 * 2 - 1
for i in range(row + 1):
    middle = (row - i) * 2 - 1 
    print(left * i + middle * star_mark)
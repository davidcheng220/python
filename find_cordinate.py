x, y = 0, 0
command = "ULLRDL"
# print(len(command))

match command:
    case "U":
        y = y + 1
    case "D":
        y = y - 1
    case "R":
        x = x + 1
    case "L":
        x = x - 1

for index in range(len(command)):
    # print(command[index])
    match command[index]:
        case "U":
            y = y + 1
        case "D":
            y = y - 1
        case "R":
            x = x + 1
        case "L":
            x = x - 1

print(x,y)
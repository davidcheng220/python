# write file
with open('text.txt', "w") as f:
    f.write("Hello")
    # f.close

# f = open("text.txt", "w", encoding="utf-8")
# f.write("hello")
# f.close()

# read file
with open('text.txt', "r") as f:
    s = f.read()
    f.close()

print(s)
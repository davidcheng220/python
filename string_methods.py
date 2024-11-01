# init string
s = "Hello"*5
print(s)

# pass string to new sting
s = s.replace("Hello" , "Bye")
print(s)

# when seeing "-" split in orders 
d = "2024-11-01"
ds = d.split("-")
print(ds)

# join date from string to xxxx/xx/xx
dj = "/".join(ds)
print(dj)

# put 2024 to last order
ds_1 = "/".join(ds[::-1])
print(ds_1)

# init string 
string = "   \n   abc \t   \n"
# print string in strip() removing white spaces
print(string.strip())
# left strip and right strip white spaces
print(string.lstrip())
print(string.rstrip())
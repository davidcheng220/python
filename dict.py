person = {
    'name': "David",
    'height': 180
}

print(person)

print(person["name"])

person["name"] = "Hello"

person["height"] = person["height"] + 5
print(person)

del person['name']
print(person)
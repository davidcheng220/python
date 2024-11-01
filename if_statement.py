

# bmi = weight(kg) / height(m) ^ 2

# keep asking when user input the height is lower than 100
# infinity loop need, break is required, if not the loop will keep running
while True:
    weight = int(input("input your weight(kg): "))
    height = int(input("input your height(cm): "))
    if height < 100:
        print("please enter height again")
    else:
        break

formula = weight / (height / 100) ** 2
bmi = round(formula, 2)

print("your bmi: ", bmi)

if bmi > 25:
    print("Over weight")
elif bmi < 24.9 and bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
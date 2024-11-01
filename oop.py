class Person:
    def __init__(self, weight, height) -> None:
        self.weight = weight
        self.height = height

    def getCalc(self):
        calc = self.weight / ((self.height / 100) **2)
        return round(calc, 2)
    
    def getInfo(self):
        print("weight: ", self.weight)
        print("height: ", self.height)
    
    def getRange(self):
        if self.getCalc() > 35:
            print("Overweight")
        else:
            print("Normal")

p1 = Person(80, 180)
print(Person.getCalc())
Person.getInfo()
Person.getRange()
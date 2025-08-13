class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")
    def ageUpdate(self, isBirthday):
        if isBirthday:
            self.age += 1
            print(f"It's my birthday! Now I ({self.name}) am {self.age}.")
        else:
            print(f"No birthday for {self.name} today.")
    def nameUpdate(self, newName):
        print(f"My name was {self.name}. My new name is {newName}.")
        self.name = newName


p1 = Person("Kathy", 22)
p2 = Person("Caleb", 27)

p1.greet()
p2.greet()

p1.ageUpdate(True)

p2.nameUpdate("Charles")
import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def greet(self):
        print(f"Hello, I am a student, and my name is {self.name}. My grade is {self.grade}%.")

    def study(self):
        gradeImp = random.randint(1, 3)
        self.grade += gradeImp
        print(f"I studied for {random.randint(1, 5)} hour(s) and improved my grade by {gradeImp}%!\n"
              f"Now my grade is {self.grade:.2f}%!")

p1 = Person("James", 23)
p2 = Student("Kaylee", 19, round(random.uniform(70, 100.01), 2))

p1.greet()
p2.greet()

p2.study()
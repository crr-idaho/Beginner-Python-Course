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

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade:.2f}"

    def greet(self):
        print(f"Hello, I am a student, and my name is {self.name}. My grade is {self.grade:.2f}%.")

p1 = Student("Kevin", 25, 98.6)

print(p1)
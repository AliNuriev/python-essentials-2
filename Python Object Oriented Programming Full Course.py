class Car:
    def __init__(self, model, year, color, for_sale): #constructor method to construct object, initialization function
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stoped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")



car1 = Car("Mustang", 2026, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Porsche", 2003, "Grey", False)

print(car1) #memory address
print(car1.model, car1.year)
print(car2.model, car2.year)
print(car3.model, car3.year)

car1.drive()
car2.stop()
car3.describe()

print(end = '\n\n')

# -------------------- #

class Student:

    class_year = 2027
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Ray", 25)
student2 = Student("Ali", 22)
student3 = Student("Mike", 23)
student4 = Student("Dom", 24)

print(student1.name, student1.age, Student.class_year, Student.num_students)
print(student2.name, student2.age, Student.class_year, Student.num_students)
print(student3.name, student3.age, Student.class_year, Student.num_students)

print(f"My grad class of {Student.class_year} has {Student.num_students} students")


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

print(f"My grad class of {Student.class_year} has {Student.num_students} students", end = '\n\n')

# Class INHERITANCE #

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive= True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    pass

dog = Dog('Scooby')
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name, dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(end = '\n\n')

# multiple and multilevel INHERITANCE

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}  is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class  Prey(Animal):
    def flee(self):
        print(f'{self.name} is fleeing')

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Buggs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.flee()
fish.sleep()

rabbit.flee()

print(end = '\n\n')

# abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# vehicle = Vehicle() # we cant instantiate , only via children

class Car(Vehicle):

    def go(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("you ride the motorcycle")

    def stop(self):
        print("you stop the motorcycle")

motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("you anchor the boat")

boat = Boat()
boat.go()
boat.stop()

print(end = '\n\n')

# SUPER()

from math import pi

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'It is {self.color} and {"filled" if self.is_filled else "not filled"}')

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) # super() or Shape.__init__
        self.radius = radius

    def describe(self):
        super().describe() #used parents method as well!
        print(f'It is a circle with an area of {self.radius**2 * pi}cm squared ')
    #method overwriting - we used describe() in a child, not parents

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe() #used parents method as well!
        print(f'It is a square with an area of {self.width**2}cm squared ')
    #method overwriting - we used describe() in a child, not parents

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe() #used parents method as well!
        print(f'It is a triangle with an area of {self.width * self.height / 2}cm squared ')
    #method overwriting - we used describe() in a child, not parents

circle = Circle("Red", True, 13)
square = Square('blue', False, 6)
triangle = Triangle('Yellow', True, 10, 5)

print(circle.color)
print(circle.is_filled)

print(square.color)
print(square.is_filled)
print(f"width of square is {square.width}cm")

square.describe()

circle.describe()

triangle.describe()

print(end = '\n\n')

# Polymorphism - many forms

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle (Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius) # calling superclass
        self.topping = topping



shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("margarita", 15)]

for shape in shapes:
    print(f"{shape.area()} cm2")

print(end='\n\n')

# Duck typing - another method of achieving polymorphism. Object must have the minimum necessary attributes/methods

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:

    alive = False

    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive, end='\n\n')

# Aggregation - one object contains references to other INDEPENDENT objects "has - a" relation

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("NY public library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkein")
book3 = Book("The Color of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for book in library.list_books():
    print(book, end = "\n\n")

# composition - object owns its components, which cannot exist independently

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model}, {self.engine.horse_power}(hp), {self.wheels[0].size}"

car1 = Car('Ford', 'Mustang', 500, 18)
car2 = Car('Porsche', '911', 800, 15)

print(car1.display_car())
print(car2.display_car(), end = '\n\n')

# nested Classes

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company = Company("Krusty Krab")
company1 = Company('Chum Bucket')

company.add_employee('Eugine', "Manager")
company.add_employee('Spongebob', "Cook")
company.add_employee('Squidward', 'Cashier')

company1.add_employee('Sheldon', 'manager')
company1.add_employee('Karen', 'Assistant')

for employee in company1.list_employees():
    print(employee)

print(end = '\n\n')

# instance and static methods
# instance - all used before
# static - best for utility functions that don't need access to class data.
#### работает с тем, что в скобках у него. не рабоатет с обьектом

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions

employee1 = Employee('Eugune', 'Manager')
employee2 = Employee('Squidward', 'Cashier')
employee3 = Employee('Spongebob', 'Cook')

print(Employee.is_valid_position('Scientist'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info(), end = "\n\n")

# class methods - operations with the class itself, working with class variables

class Students:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count:.2f} is the Average"

student1 = Students('Ali', 3.68)
student2 = Students('Ray', 4.00)
student3 = Students('Nic', 3.21)

print(Students.get_count())
print(Students.get_avg_gpa(), end = '\n\n')

# Magic methods

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):

        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.num_pages
        else:
            return f'Key {key} was not found'

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book('Harry Potter', 'J.K. Rowling', 223)
book3 = Book('Crime and Punishment', 'F. M. Dostoyevski', 345)

print(book1 == book3)
print(book2 > book3)
print(book2 + book3)
print('Crime' in book1)
print(book1['title'])
print(book3['author'])
print(book2['Audio'])





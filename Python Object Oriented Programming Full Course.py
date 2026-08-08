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
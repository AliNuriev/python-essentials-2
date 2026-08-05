class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val):
        self.__second = val

object_1 = ExampleClass()
print(object_1.__dict__)

object_2 = ExampleClass(2)
object_2.set_second(3) #use the method from class
print(object_2.__dict__)

object_3 = ExampleClass(4)
object_3.__third = 4
print(object_3.__dict__, end = '\n\n')

# ----------- #

class ExampleClass1:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass1.counter += 1

obj1 = ExampleClass1()
print(obj1.__dict__, obj1.counter)

obj2 = ExampleClass1(4)
print(obj2.__dict__, obj2.counter)

obj3 = ExampleClass1(12)
print(obj3.__dict__, obj3.counter)



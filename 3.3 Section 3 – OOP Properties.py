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
print(obj3.__dict__, obj3.counter, end = '\n\n')

# ----------- #


class ExampleClass2:
    varia = 1
    def __init__(self, val):
        ExampleClass2.varia = val

print(ExampleClass2.__dict__)
example_object = ExampleClass2(2)

print(ExampleClass2.__dict__)
print(example_object.__dict__, end = '\n\n')


# ----------- #

class ExampleClass3:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

obj4 = ExampleClass3(1)
print(obj4.a)

try:
    print(obj4.b)
except AttributeError:
    pass

print(hasattr(ExampleClass3, "a"))
print(hasattr(ExampleClass3, "b"))


print(hasattr(obj4, "a"))
print(hasattr(obj4, "b"))


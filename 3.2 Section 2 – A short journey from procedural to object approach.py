stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop(), end = "\n\n")


class Stack:
    def __init__(self):
        print('Hi!')

stack_object = Stack()
print(end = "\n\n")


class Stack:
    def __init__(self):
        self.__stack_list = [2, 4, 6, 8]

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# When any class component has a name starting with two underscores (__),
# it becomes private – this means that it can be accessed only from within
# the class.

# You cannot see it from the outside world.
# This is how Python implements the encapsulation concept.

stack_object = Stack()

stack_object.push(1)
stack_object.push(2)
stack_object.push(3)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop(), end = "\n\n")

stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop(), end = "\n\n")

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

s = AddingStack()

s.push(10)
s.push(12)
s.push(14)

print("Beginning sum:", s.get_sum())

print(s.pop())
print(s.pop())

print("Sum after getting rid of last two var:", s.get_sum(), end = "\n\n")


stack_object_3 = AddingStack()

for i in range(10):
    stack_object_3.push(i)

print(stack_object_3.get_sum())

for i in range(5):
    print(stack_object_3.pop())

print("End sum:", stack_object_3.get_sum())




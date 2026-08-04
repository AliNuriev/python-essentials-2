class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, var):
        self.__stack.append(var)

    def pop(self):
        var = self.__stack[-1]
        del self.__stack[-1]
        return var

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)

stack_1 = CountingStack()

for i in range(10):
    stack_1.push(i)
    stack_1.pop()

print(stack_1.get_counter())


def reciprocal(x):
    try:
        x= 1 / x
    except ZeroDivisionError:
        print("Division failed")
        x = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
    return x

print(reciprocal(2))
print(reciprocal(0), end = "\n\n")

# Exception is a class!!

try:
    i = int('Hello!')
except Exception as e:
    print(e)
    print(e.__str__(), end = "\n\n")

# exception tree

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
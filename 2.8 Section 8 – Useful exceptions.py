from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

assert angle % 180 != 90 # when argument is False, None, 0
print(tan(radians(angle)), end = '\n\n')

# --------------------------------#

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done!', end = '\n\n')

# --------------------------------#

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.', end = '\n\n')

# --------------------------------#

dictionary = {"a":"b", "b":"c", "c":"d"}
ch = "a"

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print("no such key ", ch)


# LAB reading ints safely

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            num = int(input(prompt))
            ok = True
        except ValueError:
            print('Enter an int!')
        if ok:
            ok = num >= min and num <= max
        if not ok:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return num

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)





import math
for elem in dir(math):
    print(elem, end = ', ')

#------------------------------------------#

print(end = '\n\n')
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi/2.)
print(sin(ar)/cos(ar) == tan(ar))
print(asin(sin(ar)) == ar, end = '\n\n')

#------------------------------------------#

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0), end = '\n\n')

#------------------------------------------#

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y)) #the largest integer less than or equal to x
print(floor(-x), floor(-y))
print(ceil(x), ceil(y)) #the smallest integer greater than or equal to x
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y)) #отбрасывание дробной части числа
print(trunc(-x), trunc(-y), end = '\n\n')

#------------------------------------------#

from random import random #produces a float number x coming from the range (0.0, 1.0)

for i in range(5):
    print(random())

print(end = '\n\n')

from random import random, seed

seed(0) #creates unchangable set of random values
# the pseudo-random values emitted from the random module will be exactly the same.
for i in range(5):
    print(random())

from random import randrange, randint

print(randrange(1), end=' ') # right-sided exclusion
print(randrange(0, 1), end=' ') # right-sided exclusion
print(randrange(0, 1, 1), end=' ') # right-sided exclusion
print(randint(0, 1))

from random import randint

for i in range(10):
    print(randint(1, 10), end=',') #some elements are not unique

print(end = '\n\n')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10), end = '\n\n')


#------------------------------------------#
from platform import platform, machine, processor, system, version

print(platform(aliased = False, terse = False))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version(),end = '\n\n' )

from platform import python_implementation, python_version_tuple

print(python_implementation())

for i in python_version_tuple():
    print(i)
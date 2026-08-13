class Fib:
    def __init__(self, nn):
        print('__init__')
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        res = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, res
        return res

class Class:
    def __init__(self, n):
        self.__fibonacci = Fib(n)

    def __iter__(self):
        print('Class iter')
        return self.__fibonacci

object = Class(10)

for i in object:
    print(i)

print(end = "\n\n")

# yield generator

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

print(end = "\n\n")
# Тело начнёт работать только когда у
# генератора попросят первое значение.

# return — «вот ответ, я закончил».
# Функция умирает, всё внутри неё исчезает.

# yield — «вот очередное значение, я подожду».
# Функция замирает, но не умирает.
# Все переменные остаются на месте, помнится строка, где остановились.

# fibonaccii generator
def fib1(n):
    p1 = p2 = 1
    for i in range(n):
        if i < 0:
            yield 1
        else:
            p1, p2 = p2, p1+p2
            yield p2

print(list(fib1(10)),end = "\n\n")

# first n powers of 2 generator
def power_of_2(n):
    yield [i**2 for i in range(n)]

for i in power_of_2(10):
    print(i)

print(end = "\n\n")

# НАГЛЯДНОЕ СРАВНЕНИЕ
# генератор - ленивый итератор - вычисления откладывается до момента когда
# результат фактически потребуется
def power_of_3(n):
    list_of_power_3 = []
    for i in range(n):
        list_of_power_3.append(i**3)
    return list_of_power_3

print(power_of_3(12))

def power_3(n):
    for i in range(n):
        yield i**3

print(list(power_3(12)))

print(end = "\n\n")
# У каждого вызова функции есть фрейм — область памяти с локальными переменными
# и позицией исполнения. Обычно фрейм создаётся при вызове и уничтожается при return.
#
# У генератора фрейм не уничтожается на yield — он откладывается в сторону и ждёт
# следующего next. Отсюда и память о переменных, и продолжение с нужной строки.

def fib_gen(n):
    pp = p = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = pp + p
            pp, p = p, n
            yield n

print(list(fib_gen(10)), end = "\n\n")

# list comprehensions crap

list_1 = []

for i in range(10):
    list_1.append(10 ** i)

list_2 = [10**i for i in range(10)]

print(list_1)
print(list_2,end = "\n\n")

# FOR CONDITION EXPRESSIONS:
# expression_one if condition else expression_two

the_list = []

for x in range(10):
    the_list.append(1 if x%2 == 0 else 0)

print(the_list)

the_list1 = [1 if x%2 == 0 else 0 for  x in range(10)]
print(the_list1, end = "\n\n")

# List comprehensions vs. generators

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# list is created as a whole and exists after execution of the loop
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
# there is no list at all – there are only subsequent values
# produced by the generator, one by one.
# генератор выдает только последующие значения - одно за другим

for v in the_list:
    print(v, end = ' ')
print()
print(f"Lenght is: {len(the_list)}")

for v in the_generator:
    print(v, end = ' ')
print()
# значения вычисляются в цикле по одному и нигде не накапливаются

try:
    print(len(the_generator))
except Exception as e:
    print(e)

print(end = "\n\n")

# LAMBDA functions

# lambda parameters: expression

two = lambda: 2
sqr = lambda x: x*x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end = '')
    print(pwr(a, two()))

print(end = "\n\n")

def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep = '')

def poly(x):
    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)
print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2- 4 * x + 2)

print(end = "\n\n")

# MAP() function

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2**x, list_1))
print(list_1, list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end= ' ')

print()
# FILTER() function

from random import seed, randint

seed(1) # разный параметр - разный набор, оставишь 1 - будет первая рандомная комбинация всегда

data = [randint(-10,10) for x in range(5)] # pick 5 random numbers in [-10, 10]
filtered = list(filter(lambda x:  x % 2 == 0, data))

print(data)
print(filtered, end = "\n\n")


# EVEN - X % 2 == 0
# ODD - X % 2 == 1

# map - возьми элемент и преобразуй его
# filter - проверяет каждый элемент исходного списка
# с помощью функции и оставляет только те элементы,
# для которых функция вернула True

# CLOSURES

def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())


def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(10):
    print(i, fsqr(i), fcub(i))

# closure особенно полезен, когда ты хочешь
# создавать много похожих функций с разными
# внутренними настройками, не передавая эти настройки каждый раз вручную


def discount(dis):
    def apply(price):
        return price * (1-dis)
    return apply

vip_disc = discount(0.4)
student_disc = discount(0.3)

for i in range(100, 105):
    print(i, vip_disc(i), student_disc(i))



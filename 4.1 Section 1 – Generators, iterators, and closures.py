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

print(list(fib_gen(10)))

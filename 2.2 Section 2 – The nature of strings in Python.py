multiline = """Line #1
Line #2"""

print(len(multiline), end = "\n\n")

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4, end = "\n\n")

# demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '

print(ord(char_1))
print(ord(char_2))

print(chr(97))
print(chr(945), end = "\n\n")

# indexing
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end = ' ')

print()

# iterating
for char in the_string:
    print(char, end = ' ')

print(end = "\n\n")

# slicing

alpha = 'abcdefg'

print(alpha[1:3])
print(alpha[3:])
print(alpha[:4])
print(alpha[3:-2])
print(alpha[::3]) # take every 3rd char
print(alpha[1::2], end = "\n\n") # start from 1st,take every 2 char

alphabet = "abcdefghijklmnopqrstuvwxyz"
print('f' in alphabet)
print('gay' in alphabet)

alphabet = alphabet + "gay"
print(alphabet, end = "\n\n")

# min(), max() functions return the smallest/largest character based on ASCII/Unicode code point order.
print(min("aAbByYzZ"))
print(max("aAbByYzZ"))

t = 'fire'
print('[' + min(t) + ']')
print('[' + max(t) + ']')

t = [0, 1, 2]
print(min(t))
print(max(t), end = "\n\n")

# finds where the letter occurs
print('aAbByYzZaA'.index('b'), end = "\n\n")

# makes a list
print(list("abcabc"), end = "\n\n")

# counts how many "b" letters there are in string
print("abcabc".count("b"))
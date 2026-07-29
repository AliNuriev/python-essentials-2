print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
try:
    print('10' > 10)# error!!!
except TypeError:
    print('cant do it', end = '\n\n')

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2, end = '\n\n')

list2 =  ['omega', 'alpha', 'pi', 'gamma']
list2.sort()
print(list2, end = '\n\n')


# convert number to string
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + " " + sf)

# convert string to number
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
print(itg + flt)

for lin in range(5):
    print('1')

for lin in range(5):
    print('1', '1', '1')

print( end = '\n\n')

digits = [
    ["###", "# #", "# #", "# #", "###"],   # 0
    ["  #", "  #", "  #", "  #", "  #"],   # 1
    ["###", "  #", "###", "#  ", "###"],   # 2
    ["###", "  #", "###", "  #", "###"],   # 3
    ["# #", "# #", "###", "  #", "  #"],   # 4
    ["###", "#  ", "###", "  #", "###"],   # 5
    ["###", "#  ", "###", "# #", "###"],   # 6
    ["###", "  #", "  #", "  #", "  #"],   # 7
    ["###", "# #", "###", "# #", "###"],   # 8
    ["###", "# #", "###", "  #", "###"],   # 9
]

def print_number(num):
    for row in range(5):
        line = ''
        for d in str(num):
            line += digits[int(d)][row] + ' '
        print(line)

print_number(int(input('number pls: ')))



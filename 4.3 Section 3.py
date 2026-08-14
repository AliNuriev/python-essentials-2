from os import strerror

try:
    counter = 0
    stream = open("C:/Users/alnur/OneDrive/Desktop/text.txt")
    char = stream.read(1)
    while char != "":
        print(char, end = '')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharecters in this file:", counter, end = "\n\n")
except IOError as a:
    print('An error occured: ', strerror(a.errno))

try:
    counter = 0
    stream = open("C:/Users/alnur/OneDrive/Desktop/text.txt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCharecters in this file:", counter, end = "\n\n")
except IOError as a:
    print('An error occured: ', strerror(a.errno))

# read(1) - один символ.
# read() без аргумента - всё, что осталось от текущей позиции до конца.

try:
    character_counter = line_counter = 0
    stream = open("C:/Users/alnur/OneDrive/Desktop/text.txt")
    line = stream.readline()
    while line != "":
        line_counter += 1
        for char in line:
            print(char, end = "")
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file: ", line_counter, end = "\n\n")
except IOError as e:
    print("I/O Error occured: ", strerror(e.errno))

# readline() читает от текущей позиции до ближайшего перевода строки

stream = open("C:/Users/alnur/OneDrive/Desktop/text.txt")
print(stream.readlines(20))
print(stream.readlines(17))
print(stream.readlines(50), end = "\n\n")
# readlines(20) - читает целые строки, пока суммарно не превысит 20 символов.
# Строку посередине не режет. Позиция в файле сдвигается,

stream.close()

try:
    ccnt = lcnt = 0
    s = open("C:/Users/alnur/OneDrive/Desktop/text.txt")
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for char in line:
                print(char, end='')
                ccnt += 1
            lines = s.readlines(20)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


try:
    ccnt = lcnt = 0
    for line in open("C:/Users/alnur/OneDrive/Desktop/text.txt", 'rt'):
        lcnt += 1
        for char in line:
            print(char, end = '')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# write() - ожидает строку, которую вложим в новый файл
try:
    file = open('C:/Users/alnur/OneDrive/Desktop/newfile.txtd', "wt")
    for i in range(10):
        file.write('line #' + str(i+1) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

print('\n\n')

# BYTEARRAYS
# Must be an integer value in bytearray
# Must be between 0-255

data = bytearray(10)
# creates an object with 10 bytes, all 0

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10-i

try:
    bf = open('C:/Users/alnur/OneDrive/Desktop/file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print('\n\n')

# readinto() - перезаписывает , не присваивает
try:
    binary_file = open('C:/Users/alnur/OneDrive/Desktop/file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end = ' ')

except IOError as e:
    print(strerror(e.errno))
print('\n\n')


## 1. Разминка: паспорт файла

# Файл: `server.log`
# Напиши функцию `file_stats(path)`, которая печатает:
# - сколько строк в файле
# - сколько символов
# - сколько слов (подсказка: `line.split()` даёт список слов)
# Проверь себя: должно получиться 15 строк.
# *Что тренируешь:* `with`, итерация по файлу, `len()`.
try:
    def file_stats():
        with open("server.log") as f:
            linc = charc = wordc = 0
            line = f.readline()

            while line != "":
                linc += 1
                wordc += len(line.split())
                for char in line:
                    charc += 1
                line = f.readline()
        print('сколько строк в файле: ', linc)
        print('сколько символов:', charc)
        print('сколько слов: ', wordc)

    file_stats()

except Exception as e:
    print(e)

## 2. Фильтр

# **Файл:** `server.log`

# Прочитай лог и запиши в новый файл `errors.log` только строки со словом `ERROR`.
# В конце напечатай, сколько строк отобрано.
# Подсказка: проверка на вхождение - это `if "ERROR" in line`.
# Проверь себя: должно быть 4 строки.
# *Что тренируешь:* чтение и запись одновременно, режим `'w'`.


try:
    with open('server.log') as f, open('errors.log', 'wt') as e:
        for line in f:
            if "ERROR" in line:
                e.write(line)
except Exception as ex:
    print(ex)


## 3. Дозапись

# **Файл:** `server.log`
# Напиши функцию `add_log(path, level, message)`, которая дописывает строку
# в **конец** лога, не стирая существующее. Формат строки как в файле:
# `ДАТА ВРЕМЯ УРОВЕНЬ сообщение`.
# Дату и время бери текущие:
# ```python
# from datetime import datetime
# now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Вызови её три раза и убедись, что старые строки на месте.
# *Что тренируешь:* режим `'a'` - это то, чего курс почти не показывает,
# а на практике он нужен постоянно (логи, накопление результатов).

from datetime import datetime

try:
    def add_log(path, level, message):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(path, 'at') as f:
            f.write(f"{now} {level} {message}\n")

    add_log('server.log', 'INFO', 'Report generated')
    add_log('server.log', 'WARNING', 'Disk usage 88%')
    add_log('server.log', 'ERROR', 'Connection lost')

except Exception as exc:
    print(exc)






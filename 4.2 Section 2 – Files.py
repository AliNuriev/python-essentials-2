# stream = open(file, mode = 'r', encoding = None)
# mode = 'r' - read, must exist

# mode = 'w' - write, if it doesn't exist it will be created;
# if it exists, it will be truncated to the length of zero (erased)

# mode = 'a' - append,if it doesn't exist, it will be created;
# if it exists the virtual recording head will be set at the end of the file
# (the previous content of the file remains untouched)

# mode = 'r+', must exist and has to be writeable

# mode = 'w+'- write and update

# rt - read text file
# rb - read BINARY file
try:
    stream = open("C:/Users/alnur/OneDrive/Desktop/sample.txt", "rt")
    stream.close()
except Exception as exc:
    print('Cannot open the file:', exc)


import sys

# три потока которые пайтон открывает сам еще до начала кода.
# sys.stdin - стандартный ввод, открыт на чтение, когда пишу input() - данные приходят именно с этого потока
# sys.stdout - стандартный вывод, открыт на запись, print() - данные идут с этого стрима
# sys.error - стандартный вывод, но предназначен только для ошибок

# errno - у исключения есть атрибут с числовым кодом ошибки

# ENOENT — файла или папки не существует
# EACCES — нет прав. Файл только для чтения, а ты пишешь
# EISDIR — подсунул папку вместо файла
# ENOSPC — диск забит

import errno

try:
    s = open("C:/Users/alnur/OneDrive/Desktop/sample1.txt", "rt")
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("This file doesn't exist, error no.", exc.errno)
    else:
        print('The error number is: ', exc.errno)

from os import strerror

# outputs the meaning of the error
try:
    s = open("C:/Users/alnur/OneDrive/Desktop/sample1.txt", "rt")
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print(strerror(exc.errno))

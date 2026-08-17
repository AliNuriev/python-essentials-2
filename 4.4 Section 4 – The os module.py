import os
# os.mkdir('my_1st_directory')
# print(os.listdir())

os.makedirs('my_1st_directory/my_second_directory')
os.chdir('my_1st_directory')

print(os.listdir()) # gives the list of files in the current directory

print(os.getcwd()) # gives the path to the directory we are in

os.chdir('my_second_directory')
print(os.getcwd()) # gives the path to the folder we've created and where we at rn

os.chdir('..') # вернулись на стэп назад
os.rmdir('my_second_directory')

os.chdir('..')
print(os.listdir())
print(os.listdir())

returned_value = os.system("mkdir my_3rd_directory")
print(returned_value)

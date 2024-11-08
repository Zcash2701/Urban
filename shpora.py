import os

print(os.getcwd())                   # Абсолютный путь
os.mkdir('dir_name')

if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')              # Создание директории
    os.chdir('second')              # Переход в директорию
    print(os.getcwd())

os.makedirs(r'second\third\fourth') # Создание вложенных директорий
print(os.listdir())                 # Содержимое


directory = '.'

for i_dir in os.walk(directory):
    print(i_dir)

files = [file for file in os.listdir() if os.path.isfile(file)]
dirs = [dir for dir in os.listdir() if os.path.isdir(dir)]
print(files)
print(dirs)

print(os.startfile(files[3]))
print(os.stat(files[2]).st_size)        # инфа о файле  .st_size размер файла

os.system('pip install random')        # запуск команды в терминале
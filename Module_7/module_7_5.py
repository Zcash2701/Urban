import os
import time

files = [file for file in os.listdir() if os.path.isfile(file)]
for i_file in files:
    file_path = os.path.join('.', i_file)
    file_time = os.stat(i_file).st_mtime
    formated_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
    file_size = os.stat(i_file).st_size
    parant_dir = os.pardir
    print(
        f'Обнаружен файл: {i_file}, '
        f'Путь: {file_path}, '
        f'Размер: {file_size} байт, '
        f'Время изменения: {formated_time}, '
        f'Родительская директория: {parant_dir}')




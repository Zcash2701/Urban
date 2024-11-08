def custom_write(file_name, strings):
    temp_dict = dict()
    file = open(file_name, 'a', encoding='utf8')
    str_count = 1

    for i_str in strings:
        temp_tuple = (str_count, file.tell())
        temp_dict[temp_tuple] = i_str
        file.write(f'{i_str}\n')
        str_count += 1
    return temp_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


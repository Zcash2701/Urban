first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (abs(len(param[0]) - len(param[1])) for param in zip(first, second) if len(param[0]) != len(param[1]))
second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)))

print(list(first_result))
print(list(second_result))
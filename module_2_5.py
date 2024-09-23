import random

def get_values():
    result = random.randint(0, 99)
    return result

def get_matrix(n, m):
    matrix = list()
    for i in range(n):
        temp_matrix = list()
        matrix.append(temp_matrix)
        for j in range(m):
            value = get_values()
            matrix[i].append(value)
    return matrix


n = int(input('Введите колличество строк: '))
m = int(input('Введите колличество столбцов: '))
print(get_matrix(n, m))

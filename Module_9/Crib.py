my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers_2 = [9, 2, 6, 1, 5,]

result = [x * 3 for x in my_numbers] # обычный list коприкейшнс

result_1 = [x * 2 for x in my_numbers if x > 5]  # c условием

result_2 = [x * 2 if x > 2 else x * 10 for x in my_numbers]         # условие и изменение операций над элементом
result_3 = [x * 2 if type(x) == str else x * 5 for x in my_numbers] # условие и изменение операций над элементом

result_4 = [x * y for x in my_numbers for y in my_numbers_2]        # вложенные списки

result_5 = [x * y for x in my_numbers for y in my_numbers_2 if x % 2 and y // 2] # вложенные + условия

result_6 = {x * 3 for x in my_numbers}  # множество
result_7 = {x: x ** 3 for x in my_numbers}  # словарь ключ - итерируемый объект, валюе - результат вычисления


# Лямбда функция:
result_8 = lambda x: x + 1

result_9 = map(lambda x, y: x + y, my_numbers, my_numbers_2)

# Замыкающие функции / налету

def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('Херня')

    return multiplier

by_2 = get_multiplier_v1(2)

result_10 = map(by_2, my_numbers)


def get_multiplier_v2(n):
    def multiplier(x):
        return x * n

    return multiplier


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n

by_1 = Multiplier(n=3)

result_11 = by_1(x=6)

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print('Равны все 3 числа')
elif first == second or second == third or third == first:
    print('Равны 2 числа')
else:
    print('Равных чисел нет')
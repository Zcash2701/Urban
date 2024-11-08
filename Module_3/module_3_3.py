def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(a=1, b='строка', c=True)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'stringi', False]
values_dict = {'a': 1, 'b': 'stringi', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [1, 'Yes']
print_params(*values_list2, 5)

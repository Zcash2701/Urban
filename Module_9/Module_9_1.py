
def apply_all_func(int_list, *functions):
    dict_result = {}
    for func_i in functions:
        dict_result[func_i.__name__] = func_i(int_list)
    return dict_result


print((apply_all_func([6, 20, 15, 9], max, min)))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
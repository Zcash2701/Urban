def get_list_numbs():
    list_info = list()
    for i in range(3, 21):
        list_info.append(i)
    return list_info


def check_values(numb):
    temp_main_list = list()
    for i in range(1, numb):
        for j in range(1, numb):
            temp_list = list()
            if i >= numb or j >= numb:
                break
            elif numb % (i + j) == 0:
                temp_list.append(i)
                temp_list.append(j)
                if (temp_list[::-1]) not in temp_main_list:
                    temp_main_list.append(temp_list)
    return temp_main_list


def main_def():
    list_nums = get_list_numbs()
    dict_info = dict()
    for numb in list_nums:
        key_name = f'Число из первой вставки: {numb}'
        dict_info[key_name] = check_values(numb)
    return dict_info

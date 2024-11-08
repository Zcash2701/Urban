data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

"""
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'set'>
<class 'str'>
"""
def calculate_structure_sum(data):
    data_sum = 0

    if type(data) == str:
        data_sum += len(data)
        return data_sum

    elif type(data) == int:
        data_sum += data
        return data_sum

    if type(data) == list:
        while len(data) > 0:
            temp_data = data.pop()
            data_sum += calculate_structure_sum(temp_data)
        return data_sum

    elif type(data) == dict:
        for keys, value in data.items():
            data_sum = data_sum + len(keys)
            data_sum = data_sum + value
        return data_sum

    elif type(data) == set:
        for data_i in data:
            return calculate_structure_sum(data_i)

    elif type(data) == tuple:
        for i_tuple in range(len(data)):
            data_sum += calculate_structure_sum(data[i_tuple])
        return data_sum

    return data_sum

print(calculate_structure_sum(data_structure))


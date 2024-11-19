first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(name) for name in first_strings if len(name) > 5]
second_result = [(name, param) for name in first_strings for param in second_strings if len(name) == len(param)]
third_result = {name: len(name) for name in first_strings + second_strings if not len(name) % 2}

print(first_result)
print(second_result)
print(third_result)
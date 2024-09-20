#1st program
a = 9
b = 5
extent = 0.5
result = (a ** extent) * b
print('{} ** {} * {} = {}'.format(a, extent, b, result), end='\n\n')

#2st program
print(9.99 > 9.98 and 1000 != 1000.1, end='\n\n')

#3rd program
first_sum = 2 * 2 + 2
second_sum = 2 * (2 + 2)
result = first_sum == second_sum
print('{} == {} != {}'.format(first_sum, second_sum, not(result))) # :)
print(result, end='\n\n')

#4rd program
str_text = '123.456'
number = float(str_text)
number = int(((number - int(number)) * 10))
print(number)

str_text = '123.456'
number2 = int(((float(str_text)) * 10)) % 10

print(number2)
def is_prime(func):
    def wrapper(*args):
        temp = func(*args)
        for i in range(2, (temp // 2) + 1):
            if temp % i == 0:
                return f'Сложное \n{temp}'
        return f'Простое \n{temp}'
    return wrapper
@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

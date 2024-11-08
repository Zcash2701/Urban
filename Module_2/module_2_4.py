numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

count = 0
for i in range(1 ,len(numbers)):

    for j in range(1, i-1):
        if numbers[i] % numbers[j] == 0:
            not_primes.append(numbers[i])
            break
    else:
        primes.append(numbers[i])

print(primes)
print(not_primes)

# Цикл for. Элементы списка. Полезные функции в цикле
numbers, primes, not_primes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [], []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, int(i ** .5) + 1):
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime:
        primes.append(i)
print(f'Primes: {primes}\nNot_primes: {not_primes}')

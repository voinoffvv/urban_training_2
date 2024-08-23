# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for n in numbers:
    if n == 1: continue
    is_primes = True
    for i in range(2, n - 1):
        if n % i == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(n)
    else:
        not_primes.append(n)


print('Primes:', primes)
print('Not primes:', not_primes)

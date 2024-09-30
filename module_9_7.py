# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(fu):
    def wrapper(*args):
        res = fu(*args)
        if res == 1:
            print('Простое')
        for i in range(2, res - 1):
            if res % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)
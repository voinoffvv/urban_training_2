# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа
def get_multiplied_digits(number):
    str_number = str(number).replace('0','')  # убираем нули
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits('040203')
print(result)
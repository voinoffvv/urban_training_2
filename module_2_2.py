numbers = [0]*3
for i in range(3):
    numbers[i] = input(f'Введите {i+1} число: ')
    # если ввели значение, которое нельзя преобраховать в ЦЕЛОЕ, то меняем на 0
    # поскольку в условии "3 целых числа", то приводим к целому
    try:
        numbers[i] = int(numbers[i])
    except:
        numbers[i] = 0

res = len(numbers) - len(set(numbers))
print(numbers)
print('Количество одинаковых чисел:', (res if res==0 else res+1))

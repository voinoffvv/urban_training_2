numbers = [0]*3
for i in range(3):
    numbers[i] = input(f'Введите {i+1} число: ')
res = len(numbers) - len(set(numbers))
print('Количество одинаковых чисел:', (res if res==0 else res+1))

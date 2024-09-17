# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second,
# если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях
# из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = list(z for z in map(lambda x, y: len(x) - len(y), first, second) if z > 0)  # Вариант 1
first_result = list((len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))) # Вариант 2
print(first_result)

second_result = list(len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(second_result)
# Домашнее задание по уроку "Распаковка позиционных параметров".

# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a=1, b='строка', c=True):
    print(f'a={a}, b={b}, c={c}') # Функция должна выводить эти параметры.

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(0)
print_params(('a', 5),2)
print_params('HELLO',True,[0, 11, 22])
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1,2,3])

# Создайте список values_list с тремя элементами разных типов.
values_list = [54.32, 'Строка', [1, 4]]
#  Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, значениями разных типов.
values_dict = {'a': 10, 'b': [2, 3, 4], 'c': values_list}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)

# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
values_list_2 = ['str1', 100]
print_params(*values_list_2, 42)
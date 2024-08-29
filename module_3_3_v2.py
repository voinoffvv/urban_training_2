# Домашнее задание по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(f'a={a}, b={b}, c={c}')

# Создайте список values_list с тремя элементами разных типов.
values_list = [54.32, 'Строка', [1, 4]]
#  Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, значениями разных типов.
values_dict = {'a': 10, 'b': [2, 3, 4], 'c': values_list}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# Домашнее задание по уроку "Распаковка позиционных параметров".

def print_params(a = 1, b = 'строка', c = True):
    print(f'a={a}, b={b}, c={c}')

print_params(b = 25)
print_params(c = [1,2,3])

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
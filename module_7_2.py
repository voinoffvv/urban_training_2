def custom_write(file_name, strings):
    res = {}
    with open(file_name, 'w', encoding="utf-8") as file:
        i = 0
        for s in strings:
            i += 1
            res[f'({i}, {file.tell()})'] = s
            file.write(s + '\n')
        return res

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
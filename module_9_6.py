
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
def all_variants(text):
    for j in range(len(text)):
        for i in range(len(text)):
            c = text[i: j + 1:]
            if c != '':
                yield c


a = all_variants("abc")
for i in a:
    print(i)


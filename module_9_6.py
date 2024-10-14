
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
def all_variants(text):
    for i in range(len(text)):
        for j in range(i, len(text)):
            c = text[i: j + 1:]
            yield c

for i in all_variants("abc"):
    print(i)



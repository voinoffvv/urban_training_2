import os
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: x == y, first, second))
print(res)

def get_advanced_writer(file_name):
    if os.path.exists(file_name):
        pass

    def write_everything(*data_set):
        with open(file_name, 'w', encoding="utf-8") as file:
            for s in data_set:
                file.write(str(s)+'\n')
            file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall():
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)
    def first_ball(self):
        return self.__call__()

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
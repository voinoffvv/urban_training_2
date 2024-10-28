'''Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub(https://github.com/yanchuki/HumanMoveTest/blob/master/runner_and_tournament.py).
(Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start,
который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
(брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.'''

import unittest
from new_runner import Runner
from new_runner import Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        print('!@@#$$@$#@$')
        for s in cls.all_results:
            print(s)

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    def test_Tournament_1(self):
        t1 = Tournament(90, *[self.r1, self.r2, self.r3])
        self.all_results = t1.start()
        last1 : Runner = list(self.all_results[i] for i in self.all_results if i == max(self.all_results.keys())).pop()
        self.assertTrue(last1.name == 'Ник')
    def test_Tournament_2(self):
        t2 = Tournament(90, *[self.r1, self.r2, self.r3])
        self.all_results = t2.start()
        last2 : Runner = list(self.all_results[i] for i in self.all_results if i == max(self.all_results.keys())).pop()
        self.assertTrue(last2.name == 'Ник')
    def test_Tournament_3(self):
        t3 = Tournament(90, *[self.r1, self.r2, self.r3])
        self.all_results = t3.start()
        last3 : Runner = list(self.all_results[i] for i in self.all_results if i == max(self.all_results.keys())).pop()
        self.assertTrue(last3.name == 'Ник')

if __name__ == '__main__':
    unittest.main()

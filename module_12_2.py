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
        for d in cls.all_results:
            #print({k:v.name} for k, v in d)
            print(d)

    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    # добавляем в словарь номер прибытия гонщика и имя гонщика строкой (Runner.name)
    # если в словарь добавить объект класса Runner, то print не выводит его имя (почему-то, хотя __str__ реализовано)
    def add_in_all_results(self, _list):
        res = []
        for k in _list:
            res.append({k : _list[k].name})
        self.all_results.append(res)

    def test_Tournament_1(self):
        tournament = Tournament(90, *[self.r1, self.r3])
        res = tournament.start()
        #self.all_results.append(res)
        self.add_in_all_results(res)
        last : Runner = list(res[i] for i in res if i == max(res.keys())).pop() # ищем последнего бегуна
        self.assertTrue(last.name == 'Ник')

    def test_Tournament_2(self):
        tournament = Tournament(90, *[self.r2, self.r3])
        res = tournament.start()
        # self.all_results.append(res)
        self.add_in_all_results(res)
        last: Runner = list(res[i] for i in res if i == max(res.keys())).pop()  # ищем последнего бегуна
        self.assertTrue(last.name == 'Ник')

    def test_Tournament_3(self):
        tournament = Tournament(90, *[self.r1, self.r2, self.r3])
        res = tournament.start()
        # self.all_results.append(res)
        self.add_in_all_results(res)
        last: Runner = list(res[i] for i in res if i == max(res.keys())).pop()  # ищем последнего бегуна
        self.assertTrue(last.name == 'Ник')

if __name__ == '__main__':
    unittest.main()

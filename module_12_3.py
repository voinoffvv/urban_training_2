# Подготовка:
# В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
# Часть 1. TestSuit.
##     Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с
#     произвольным названием.
#     Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
#     Создайте объект класса TextTestRunner, с аргументом verbosity=2.
## Часть 2. Пропуск тестов.
##     Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
#     Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
#     is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 
# 'Тесты в этом кейсе заморожены'.
## Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.

import unittest
from module_12_1 import RunnerTest
from module_12_2 import TournamentTest


if __name__ == '__main__':
    myTestSuite = unittest.TestSuite()
    myTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    myTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    if __name__ == '__main__':
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(myTestSuite)

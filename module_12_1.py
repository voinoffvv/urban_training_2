'''
Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.
Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
'''
import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r_walk = Runner('Runner 1')
        for _ in range(10):
            r_walk.walk()
        self.assertEqual(r_walk.distance, 50)

    def test_run(self):
        r_run = Runner('Runner 2')
        for _ in range(10):
            r_run.run()
        self.assertEqual(r_run.distance, 100)

    def test_challenge(self):
        r_challenge1 = Runner('Runner 3')
        r_challenge2 = Runner('Runner 4')
        for _ in range(10):
            r_challenge1.run()
            r_challenge2.walk()
        self.assertNotEqual(r_challenge1.distance, r_challenge2.distance)

if __name__ == '__main__':
    unittest.main()
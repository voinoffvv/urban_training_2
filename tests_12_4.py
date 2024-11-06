import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r_walk = Runner('Runner 1', -5)
            for _ in range(10):
                r_walk.walk()
            self.assertEqual(r_walk.distance, 50)
            logging.info('\"test_walk\" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info = True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r_run = Runner(1)
            for _ in range(10):
                r_run.run()
            self.assertEqual(r_run.distance, 100)
            logging.info('\"test_run\" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info = True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r_challenge1 = Runner('Runner 3')
        r_challenge2 = Runner('Runner 4')
        for _ in range(10):
            r_challenge1.run()
            r_challenge2.walk()
        self.assertNotEqual(r_challenge1.distance, r_challenge2.distance)


if __name__ == '__main__':
   unittest.main()

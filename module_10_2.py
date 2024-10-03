from threading import Thread
from time import sleep

# Создание класса
class Knight(Thread):
    def __init__(self, name:str, power:int):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def __days_srt(self, n:int) -> str:
        res = 'дней'
        if str(n)[-1] in ['2', '3', '4']: res = 'дня'
        if str(n)[-1] == '1': res = 'день'
        if n in [11, 12, 13, 14]: res = 'дней'
        return res

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy_num = 100
        day = 0
        while enemy_num > 0:
            day += 1
            enemy_num = enemy_num - self.power
            if enemy_num <= 0:
                enemy_num = 0
            print(f'{self.name} сражается {day} {self.__days_srt(day)}, осталось {enemy_num} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day} {self.__days_srt(day)}!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')

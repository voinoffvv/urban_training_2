# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
# Объекты этого класса должны создаваться следующим способом - Table(1)
# Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
# Класс Guest:
# Должен наследоваться от класса Thread (быть потоком).
# Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# Обладать атрибутом name - имя гостя.
# Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
# Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
# Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
# Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
# Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
# Далее запустить поток этого гостя (start)
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).

from queue import Queue
import time
from random import randint
from threading import Thread

class Table:
    def __init__(self, number:int, guest = None):
        self.number = number
        self.guest = guest

class Guest (Thread):
    def __init__(self, name):
        Thread.__init__(self, name=name, daemon=True)
        self.name = name

    def __str__(self):
        return self.name

    def run(self):
        time.sleep(randint(1, 2))

class Cafe:
    def __init__(self, *args):
        self.tables : (Table) = list(args)
        self.queue = Queue()

    def guest_arrival(self, *args):
        guests_22 = list(args)[::-1]
        while len(guests_22) > 0:
            for t1 in self.tables:
                if t1.guest is None and len(guests_22) > 0: # если есть свободный стол, то сажать гостя за стол
                    t1.guest = guests_22.pop()
                    t1.guest.start()
                    print(f'{t1.guest} сел(-а) за стол номер {t1.number}.')
                else: # все столы заняты или гости кончились
                    if len(guests_22) > 0:
                        g22 = guests_22.pop()
                        self.queue.put(g22)
                        print(f'{g22} в очереди.')

        pass #def guest_arrival

    def discuss_guests(self):
        while True:
            for t2 in self.tables:
                if t2.guest is not None and t2.guest.is_alive() == False:
                    print(f'{t2.guest} покушал(-а) и ушёл(ушла).')
                    print(f'Стол номер {t2.number} свободен.')
                    t2.guest = None
                    if not self.queue.empty():
                        t2.guest = self.queue.get()
                        print(f'{t2.guest} вышел(-ла) из очереди и сел(-а) за стол номер {t2.number}.')
                        t2.guest.start()

            if len([t0 for t0 in self.tables if t0.guest is None]) == 0 and self.queue.empty() == True:
                break


if __name__ == '__main__':
    start_time = time.time()
    guests_names = [ 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                     'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                     ]
    guests = [Guest(name) for name in guests_names]
    tables = [Table(number) for number in range(1, 3)]
    cafe = Cafe(*tables)
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()
    print(f'Время работы кафе: {time.time() - start_time}')

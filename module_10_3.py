from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            increase = randint(50, 500)
            self.balance += increase
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {increase}. Баланс: {self.balance}.')
            sleep(0.001)
        pass

    def take(self):
        for _ in range(100):
            decrease = randint(50, 500)
            print(f'Запрос на {decrease}.')
            if self.balance >= decrease:
                self.balance -= decrease
                print(f'Снятие: {decrease}. Баланс: {self.balance}.')
                sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
                sleep(0.001)
        pass

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
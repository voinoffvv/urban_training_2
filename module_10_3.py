# Методы объекта:
# Метод deposit:
# Будет совершать 100 транзакций пополнения средств.
# Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
# Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
# После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
# Метод take:
# Будет совершать 100 транзакций снятия.
# Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
# В начале должно выводится сообщение "Запрос на <случайное число>".
# Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее
# число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
# Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.


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
            with self.lock:
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

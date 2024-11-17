import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect('not_telegram.db')
    with connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY,'
                       'username TEXT NOT NULL,'
                       'email TEXT NOT NULL,'
                       'age INTEGER,'
                       'balance INTEGER NOT NULL)')

        cursor.execute('DELETE FROM Users')  # удалим старые записи

        # Заполните её 10 записями:
        usernames = []
        for i in range(1, 11):
            username = f'user{i}'
            usernames.append(username)
            cursor.execute(
                f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', 'example{i}@gmail.com', {i * 10}, 1000)")

        # Обновите balance у каждой 2ой записи начиная с 1ой на 500:
        for i in range(1, 11):
            cursor.execute(f"UPDATE Users SET balance = 500 WHERE username IN {tuple(usernames[::2])}")

        # Удалите каждую 3ую запись в таблице начиная с 1ой:
        cursor.execute(f'DELETE FROM Users WHERE username IN {tuple(usernames[::3])}')


# **********************************************************************************************#
        # Удалите из базы данных not_telegram.db запись с id = 6.
        cursor.execute('DELETE FROM Users WHERE id = 6')

        # Подсчитать общее количество записей.
        # Посчитать сумму всех балансов.
        # Вывести в консоль средний баланс всех пользователей.
        cursor.execute('SELECT COUNT(*)  FROM Users')
        users_count = cursor.fetchone()[0]
        cursor.execute('SELECT SUM(balance)  FROM Users')
        blance_sum = cursor.fetchone()[0]

        try:
            print(f'средний баланс всех пользователей = {blance_sum}/{users_count} = {blance_sum / users_count}')
        except ZeroDivisionError:
            print('Таблица Users пуста')

        connection.commit()

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
#     id - целое число, первичный ключ
#     username - текст (не пустой)
#     email - текст (не пустой)
#     age - целое число
#     balance - целое число (не пустой)

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

        cursor.execute('DELETE FROM Users')

        # Заполните её 10 записями:
        usernames = []
        for i in range(1, 11):
            username = f'user{i}'
            sql = (
                f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', 'example{i}@gmail.com', {i * 10}, 1000)")
            cursor.execute(sql)
            usernames.append(username)

        # Обновите balance у каждой 2ой записи начиная с 1ой на 500:
        for i in range(1, 11):
            sql = f"UPDATE Users SET balance = 500 WHERE username IN {tuple(usernames[::2])}"
            cursor.execute(sql)

        # Удалите каждую 3ую запись в таблице начиная с 1ой:
        sql = f'DELETE FROM Users WHERE username IN {tuple(usernames[::3])}'
        cursor.execute(sql)

        # Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
        sql = f'SELECT username, email, age, balance  FROM Users WHERE age <> 60'
        cursor.execute(sql)
        users = cursor.fetchall()
        for user in users:
            s = f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]} '
            print(s)

        connection.commit()
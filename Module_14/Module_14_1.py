import pprint
import sqlite3
import random
from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.RU)

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#connect.commit()
#1) Заполнение таблицы:
for _ in range(10):
    username = person.username()
    email = person.email()
    age = random.randint(20, 80)
    balance = 1000
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (username, email, age, balance))


#2) Обновление баланса у чётных пользователей
cursor.execute('UPDATE Users SET balance = 5000 WHERE id % 2 != 0')

cursor.execute('SELECT * FROM Users')
data = cursor.fetchall()

#3) Удаление каждой 3 записи.  1 4 7 10
for user_id in range(0, len(data), 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (data[user_id][0],))

#4) Выборка пользователей
for user in data:
    if user[3] < 60 or user[3] > 70:
        print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')



connect.commit()
connect.close()
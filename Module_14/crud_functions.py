'''
1) Создание таблицы
    id - int
    title - text
    description
    price

2) get_all_products - возвращает все продукты

'''

import sqlite3

db_name = 'not_telegram.db'


def create_table_Products():
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Product(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
                )
                ''')

def get_all_product():
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM Product')
        products = cursor.fetchall()
        return products

def create_table_Users():
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
                )
                ''')

def add_user(username, email, age):
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (username, email, age))

def is_included(username):
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        count = cursor.execute('SELECT COUNT(*) FROM Users WHERE username=?',(username,)).fetchone()[0]
        return count

# Модуль SQLite

# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://sqlitestudio.pl/index.rvt?act=download

import sqlite3

# Подключение  к БД
db = sqlite3.connect('test_db.sqlite')

# Курсор - специальный объект для выполнения запросов
cursor = db.cursor()

# Создаём таблицу через SQL запрос
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE
)
''')

# Закрытие соединения с БД
db.close()
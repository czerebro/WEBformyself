# Модуль SQLite

# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://sqlitestudio.pl/index.rvt?act=download

import sqlite3

def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

users = [
    ('user1', 'user1@gmail.com'),
    ('user2', 'user2@gmail.com'),
    ('user3', 'user3@gmail.com'),
]

# Подключение  к БД
db = sqlite3.connect('test_db.sqlite')

#db.row_factory = dict_factory

# Курсор - специальный объект для выполнения запросов
cursor = db.cursor()

# Создаём таблицу через SQL запрос
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE
)
'''
               )

# Готовим данные для вставки в таблицу по одному
#cursor.execute("INSERT INTO users (name, email) VALUES ('Иванов', 'ivanov@gmail.com')")
#cursor.execute("INSERT INTO users (name, email) VALUES ('Петров', 'petrov@gmail.com')")
#cursor.execute("INSERT INTO users (name, email) VALUES ('Сидоров', 'sidorov@gmail.com')")
#cursor.execute("INSERT INTO users (name, email) VALUES ('Пупкин', 'pupkin@gmail.com')")

# Множественный запрос
cursor.executescript("""
INSERT INTO users (name, email) VALUES ('Краснов', 'krasnov@gmail.com');
INSERT INTO users (name, email) VALUES ('Белов', 'belov@gmail.com')
"""
                     )

# Вставить в запрос итерируемую последовательность
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

# Вставляем данные в таблицу
db.commit()

# Чтение данных из таблицы
email = 'petrov@gmail.com'

# Плохой вариант
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
res = cursor.fetchone()
print(res)
print(res[1])

# Хороший вариант
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
res = cursor.fetchone()
print(res)
print(res[1])

cursor.execute("SELECT * FROM users WHERE email = ? OR NAME = ?", (email, 'Пупкин'))
res = cursor.fetchone()
print(res)

cursor.execute("SELECT * FROM users WHERE email = :email OR NAME = :name", {'email': email, 'name': 'Пупкин'})
res = cursor.fetchone()
print(res)

cursor.execute("SELECT * FROM users")
res = cursor.fetchall()
print(res)

# Цикл для кортежа
for user in res:
    print(user[1], user[2])

# Цикл для словаря
for user in res:
    print(user['name'], user['email'])

# Если забыли прописать db.commit()
cursor.execute("INSERT INTO users (name, email) VALUES ('User4', 'user4@gmail.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('User5', 'user5@gmail.com')")

print(db.total_changes)

# Закрытие соединения с БД
db.close()
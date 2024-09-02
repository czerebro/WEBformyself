# Модули в Python
# https://docs.python.org/3/library/

import os                               # Подключение модуля
#import random as r                     # Сделали псевдоним для модуля
from random import shuffle, randint     # Импорт конкретного метода из модуля
#from random import *                   # Импорт всех методов

import libs                             # Импортирую свой модуль

print(os.getcwd())                      # C:\Users\user\PycharmProjects\WEBformyself
#print(r.randint(1, 100))               # Генерация числа от 1 до 100 включительно
print(randint(1, 100))

l = [1, 2, 3, 4, 5]
shuffle(l)                              # Shuffle перемешивает список
print(l)

print(libs.get_count('Hello', 'l'))
print(libs.get_len('Hello'))

f = libs.get_count                      # Задаём псевдоним для функции
print(f('Hello', 'l'))

print(__name__)                         # __main__ Хранится имя файла если файл откуда-то подключается

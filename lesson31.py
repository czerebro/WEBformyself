# Модуль datetime
import locale
from datetime import date                   # импортируем класс date
from datetime import datetime               # возвращает дату и время

# date
today = date.today()
print(today)                                # 2024-09-03
print(today.day)                            # 3
print(today.month)                          # 9
print(today.year)                           # 2024
print(today.weekday())                      # 0-понедельник 6-воскресенье

#datetime
now = datetime.now()                        # 2024-09-03 17:55:16.855288
now2 = datetime.today()                     # 2024-09-03 17:55:16.855289

print(now, now2)
print(now.hour)                             # 17
print(now.minute)                           # 56
print(now.second)                           # 38

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()])                  # вт

# strftime()
print(now.strftime('%a'))                   # Tue
print(now.strftime('%A'))                   # Tuesday

from locale import setlocale
setlocale(locale.LC_ALL, 'ru_Ru.UTF-8')

print(now.strftime('%a'))                   # Вт
print(now.strftime('%A'))                   # вторник

print(f'Дата: {now.strftime("%A, %d %b %Y")}')  # Дата: вторник, 03 сен 2024
print(f'Время: {now.strftime("%H:%M:%S")}') # Время: 20:33:21

print(now.strftime('%c'))                   # 03.09.2024 20:34:33
print(now.strftime('%x'))                   # 03.09.2024
print(now.strftime('%X'))                   # 20:34:57

from datetime import timedelta
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1)                                   # 2024-09-04 22:47:09.957300
print(d1.strftime('%c'))                    # 04.09.2024 22:48:52
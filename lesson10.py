# Методы строк
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

s = 'Тестовая строка'
ss = 'ТЕСТОВАЯ СТРОКа'

# len(str) - Длина строки
print(len(s))                   # 15

# str.capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
print(ss.capitalize())          # Тестовая строка

# str.center(width, [fill]) - Возвращает отцентрованную строку,
# по краям которой стоит символ fill (пробел по умолчанию)
print(s.center(30))             #        Тестовая строка
print(s.center(30, '_'))        # _______Тестовая строка________

# str.count(str, [start],[end]) - Возвращает количество непересекающихся вхождений подстроки
# в диапазоне [начало, конец] (0 и длина строки по умолчанию)
print(s.count('т'))             # 2
print(s.count('Т'))             # 1
print(s.count('о', 0, 7))       # 1 вхождение в диапазоне с 0 по 7й символ

# str.find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
print(s.find('о'))              # 4 первое вхождение начиная с 0
print(s.find('н'))              # -1 такого символа нет

# str.index(str, [start],[end]) - Поиск подстроки в строке.
# Возвращает номер первого вхождения или вызывает ValueError
print(s.index('о'))             # 4 первое вхождение начиная с 0
#print(s.index('н'))            # ValueError: substring not found

# str.replace(шаблон, замена) - Замена шаблона
print(s.replace('о', 'Ж'))      # ТестЖвая стрЖка

# str.split([символ])- Разбиение строки по разделителю. По умолчанию пробел
print(s.split())                # ['Тестовая', 'строка']
print(s.split('о'))             # ['Тест', 'вая стр', 'ка']

#str.isdigit() - Состоит ли строка из цифр
print(s.isdigit())              # False

#str.isalpha() - Состоит ли строка из букв
print(s.isalpha())              # False пробел и знаки препинания не являются буквами

#str.isalnum() - Состоит ли строка из цифр или букв
print(s.isalnum())              # False

#str.islower() - Состоит ли строка из символов в нижнем регистре
print(s.islower())              # False

#str.isupper() - Состоит ли строка из символов в верхнем регистре
print(s.isupper())              # False
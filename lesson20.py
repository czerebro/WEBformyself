# Кортежи (неизменяемый список)
from xml.etree.ElementPath import xpath_tokenizer_re

# Создание кортежа
t = ()                                  # Пустой кортеж
print(t)
t = (1, )                               # Добавили в кортеж 1ку
print(t)
t1 = (1, 2, 3)
print(type(t1))                         # <class 'tuple'>
t2 = 1, 2, 3                            # Упаковка кортежа
t3 = tuple((1, 2, 3))                   # Конструктор кортежа
t4 = tuple('Hello')                     # ('H', 'e', 'l', 'l', 'o')

# Обращение по индексу с нулевого элемента
print(t4[4])                            # o

# Сложение кортежей
t5 = t2 + t4
print(t5)                               # (1, 2, 3, 'H', 'e', 'l', 'l', 'o')

# Длина кортежа
print(len(t5))                          # 8

#  Количество элементов в последовательности
print(t5.count('l'))                    # 2
print(t5.count('x'))                    # 0

# Позиция в последовательности
print(t5.index(3))                      # 2

for i in t5:
    print(i,end=' ')                    # 1 2 3 H e l l o

# Список внутри кортежа можно изменять
t6 = (4, 5, 6, ['Hello', 'world', 7], [0, 'a', 'c', 9], 10, '!!!!!')
print('\n', t6)
t6[3][1] = '.!.'
print(t6)
t6[3].append('new')
print(t6)

# Распаковка кортежа (значений должно быть столько же сколько элементов в кортеже)
t7 = (1, 2, 3, )
x, y, z = t7
print(x, y, z)

# Поменять значения местами
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)
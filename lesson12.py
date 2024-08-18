# Оператор IF

# Операторы сравнения
print(2 == 2)               # True
print(2 != 6)               # True
print(2 >= 6)               # False
print(2 <= 4)               # True
print(2 > 6)                # False
print(2 < 4)                # True

'''
if выражение 1:
    блок кода 1
elif выражение 2:
    блок кода 2
else:
    блок кода 3
'''

x = 0
if x:
    print('Переменная x вернула ИСТИНУ')
else:
    print('Переменная x вернула ЛОЖЬ')          # Вывод

if 1:
    print('Выражение истинно')                  # Вывод
else:
    print('Выражение ложно')

light = 'blue'

if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print('Go')
else:
    print('What?')                              # Вывод

age = int(input('Сколько Вам лет? '))

if age >= 18:
    print('Добро пожаловать')
else:
    print(f'Вам {age} лет, не хватает {18 - age}')

time = 12
if time < 12 or time > 13:                      # любая из частей вернёт True выполняется
    print('Open')
else:
    print('Close')

time = 8
day = 'st'

if time >= 8 and day != 'su':                   # Обе части вернут True выполняется
    print('Open')
else:
    print('Close')

x = 0
if not x:
    print('OK')                                 # OK
else:
    print('NO')

x = 1
res = 'OK' if x else 'NO'                       # Тернарный оператор
print(res)                                      # OK
print('OK' if x else 'NO')                      # OK
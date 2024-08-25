# Изменяемые и неизменяемые объекты

x = 10
print(x, id(x))

x = 20
print(x, id(x))         # Неизменяемый

y = x
print(x, id(x))
print(y, id(y))         # Объекты разные, но ссылаются на одно значение

s = 'Hello'
print(s, id(s))
s += ' world'
print(s, id(s))         # Неизменяемый

l1 = [1, 2, 3]
l2 = l1
print(l1, id(l1))
l1.append(4)
print(l1, id(l1))         # Изменяемый(id одинаковый)
print(l2, id(l2))         # l2 ссылается на тот же список что и l1
l2 = l1.copy()
print(l2, id(l2))         # id у l2 поменялся
l2 = l1[:]                # работает как функция copy()
print(l2, id(l2))         # id у l2 поменялся

del x                     # Удаляет объект из памяти
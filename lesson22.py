# Множества - неупорядоченная коллекция элементов. Изменяемый тип

# Создание множеств
s = {'apple', 'orange', 'apple', 'pear', 'banan', 'orange'}
print(type(s))                                      # <class 'set'>
print(s)                                            # {'apple', 'banan', 'orange', 'pear'}
s2 = set('hello')                                   # Конструктор set
print(s2)                                           # {'o', 'l', 'h', 'e'}
s3 = {i for i in range(1, 11)}                      # Генератор
print(s3)                                           # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s4 = set()                                          # Пустое множество
print(s4)                                           # set()

nums = [1, 2, 3, 1, 2, 3, 2, 4, 1]
nums2 = set(nums)
print(nums2)                                        # {1, 2, 3, 4} числа упорядочивает по возрастанию
nums2 = list(set(nums2))
print(nums2)                                        # [1, 2, 3, 4] обратно в список

# Операции с множествами
a = set('abracadabra')                              # {'b', 'd', 'r', 'a', 'c'}
b = set('alacazam')                                 # {'l', 'z', 'a', 'c', 'm'}
print(a, b, sep='\n')

# Вычитание
c = a - b
print(c)                                            # {'r', 'd', 'b'}

# Объединение - все буквы которые встречаются
d = a | b
print(d)                                            # {'d', 'a', 'r', 'm', 'c', 'z', 'b', 'l'}

# Пересечение - дубли
e  = a & b
print(e)                                            # {'a', 'c'}

# Символы кроме дублей
f = a ^ b
print(f)                                            # {'m', 'z', 'l', 'r', 'd', 'b'}

# Методы для работы с множествами
# set.copy() - возвращает копию множества
s2 = s.copy()
print(s, id(s))
print(s2, id(s2))                                   # два разных множества
# set.add(elem) - добавляет элемент в множество
s.add('melon')
print(s)
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует
s.remove('apple')
#s.remove('apple2')                                 # Ошибка
print(s)
# set.discard(elem) - удаляет элемент, если он находится в множестве
s.discard('apple')
print(s)
# set.pop() - возвращает и удаляет первый элемент из множества.
# Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# set.clear() - очистка множества
s.clear()
print(s)                                            # set()

# Проверка есть ли элемент во множестве
if 'apple' in s:
    print('OK')
else:
    print('None')

# Frozenset - неизменяемый тип данных
a = frozenset('hello')
print(a)
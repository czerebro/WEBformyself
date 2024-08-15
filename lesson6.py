# Переменные

# Имя переменной должно состоять только
# из цифр, букв и знаков подчеркивания.
# И не должно начинаться с цифры.

# Примеры именования переменных
x = 1
y = 3.5
m = 6; n = 8
c, d = (7, 9)       # Множественное присваивание или распаковка кортежа
s = 'Sergey'
b = True
myvar = 50
_myvar = 100
myVar = 30
TEST = 10           # Псевдоконстанта
v = None            # Переменная неопределена

# Тип переменной
print(type(x))      # <class 'int'>
print(type(y))      # <class 'float'>
print(type(s))      # <class 'str'>
print(type(b))      # <class 'bool'>
print(v)            # None

# Функция id()
print(id(x))
print(id(y))
print(id(s))
print(id(b))

# Преведение типов
x = 5.2
print(x, type(x))   # 5.2 <class 'float'>
x = int(x)
print(x, type(x))   # 5 <class 'int'>
x = str(x)
print(x, type(x))   # 5 <class 'str'>
x = bool(x)
print(x, type(x))   # True <class 'bool'>
x = 0
print(x, type(x))   # 0 <class 'int'>
x = bool(x)
print(x, type(x))   # False <class 'bool'>
x = ''
print(x, type(x))   # <class 'str'>
x = bool(x)
print(x, type(x))   # False <class 'bool'>
x = None
print(x, type(x))   # None <class 'NoneType'>
x = bool(x)
print(x, type(x))   # False <class 'bool'>
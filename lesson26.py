# Пользовательские функции

def first_function():
    print('Hello')

first_function()                                # Hello
print(first_function())                         # Hello None


def f1(name):
    print('Hello, ' + name)

f1('John')                                      # Hello John
f1('Kate')                                      # Hello Kate


def f2(name, age):
    print(f'Hello, {name}. Your age is {age}')

f2('John', 18)                         # Hello, John. Your age is 18
f2('Kate', 20)                         # Hello, Kate. Your age is 20


def get_sum(a, b):
    print(a + b)

x, y = 2, 5
get_sum(1, 9)                               # 10
get_sum(x, y)                                    # 7


def f3(a, b):
    return a + b


print(f3(1,2))                              # 3


def f4(x, y, z = 4):                        # Именнованый аргумент z
    return x + y + z

print(f4(6, 3))                             # 13
print(f4(3, 8, 1))                          # 12


# функция с переменным количеством аргументов
# *args - кортеж с позиционными аргументами
# **kwargs - словарь с именованными аргументами
def get_sum2 (*args, **kwargs):
    print(args)
    return sum(args)


print(get_sum2(1, 2, 5))                      # (1, 2, 5)   8


def f5(**kwargs):
    print(kwargs)

f5(a=1, b=2, c=3)                               # {'a': 1, 'b': 2, 'c': 3}


def f6(m, n, *args, **kwargs):
    print(m)
    print(n)
    print(args)
    print(kwargs)

f6(1, 4, 7, 8, x='Python', y='Hello')           # 1
                                                # 4
                                                # (7, 8)
                                                # {'x': 'Python', 'y': 'Hello'}

f6(1, 4)                                        # 1
                                                # 4
                                                # ()
                                                # {}

# Описание функций (документирование)
def f7(a, b):
    """
    Возвращает сумму аргументов a и b.

    :param a: Первый операнд
    :type a: int
    :param b: Второй операнд
    :type b: int
    :return: Сумма операндов
    """
    return a + b

print(f7(4, 5))

# Области видимости локальная и глобальная
i = 5   # global
def f8():
    # i += 1                               # Ошибка. i - глобальная переменная. Только для чтения
    i = 7  # local
    j = 5
    print(i)                               # 7

# print(j)                                  # Ошибка. j - локальная переменная функции
print(i)                                    # 5
f8()                                        # 7
print(i)                                    # 5


h = 9
def f9():
    global h                                # Разрешает изменять h внутри функции
    h += 1
    print(h)

print(h)                                    # 9
f9()                                        # 10

#  Функция внутри функции
l = [1, '2', 3]

def func_l(l):
    def get_mult(x):
        return x * 2
    return [get_mult(i) for i in l]

print(func_l(l))                            # [2, '22', 6]

def func_ll(l):
    def get_mult(x):
        if isinstance(x, int):              # Если x типа int
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)] # Если get_mult True то записываем в список

print(func_ll(l))                            # [2, 6]


def func_lll(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))             # Для каждого элемента списка l делаем get_mult

print(func_lll(l))                            # [2, '22', 6]
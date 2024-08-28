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


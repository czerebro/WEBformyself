# Декораторы
from lesson34 import title


# Передаём функцию как параметр другой функции
def hello():
    return 'I\'m func Hello'

def super_func(func):
    print('Im Super func!')
    print(func())

super_func(hello)

# Функцию можно присваивать переменной
test = hello
print(test())

# Пример декораторов
def my_decorator(func):
    def func_wrapper():
        print('Before')
        func()
        print('After')
    return func_wrapper

@my_decorator
def func_test():
    print("Im func_test")

#example = my_decorator(func_test)
#example()

func_test()

# Второй пример декоратора
def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', ' ')
        return title
    return wrapped

@make_title
def hi():
    return 'hello, word'

print(hi())
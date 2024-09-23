# Классы для подключения в урок 37

class Person:
    def __init__(self, name):
        self.name = name
        # защищенное свойство но доступное по имени
        self._age = 20
        # защищенное свойство. выдаст ошибку при прямом обращении
        self.__age2 = 30

    def get_age(self):
        return self.__age2

    def set_age(self, value):
        if value in range(1, 101):
            self.__age2 = value
        else:
            print('Неверный возраст')

    # Метод геттер - задаётся первым
    @property
    def age(self):
        return self.__age2

    # Метод сеттер - задаётся после геттера
    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age2 = value
        else:
            print('Неверный возраст')

    def print_info(self):
        print(f'Name: {self.name}. Age: {self._age}. Age2: {self.__age2}')
# Классы для подключения в урок 37

class Person:
    def __init__(self, name, age):
        self.name = name
        # защищенное свойство но доступное по имени
        self._age = age
        # защищенное свойство. выдаст ошибку при прямом обращении
        self.__age2 = age

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

# Наследование
class Employee(Person):
    company = 'Google'

    def more_info(self):
        print(f'{self.name} works in {self.company}')

# Полиморфизм

class Pupil(Person):

    def __init__(self, name, age, school):
        super().__init__(name, age)
        # super(Pupil, self).__init__(name, age)
        self.school = school

    def more_info(self):
        print(f'{self.name} study in № {self.school}')

    def print_info(self):
        super().print_info()
        print(f'School № {self.school}')

    def __str__(self):
        # return f'Name: {self.name}'
        # Выдаст название класса из которого он вызван
        return f'Class: {self.__class__.__name__}'
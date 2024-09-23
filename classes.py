# Классы для подключения в урок 37

class Person:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f'Hello! My name is {self.name}')
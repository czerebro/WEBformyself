# Наследование - создание нового класса на основе существующего
# Наследует все открытие свойства и методы

from classes import Person, Employee

person = Person('Kate', 18)
person.print_info()

employee = Employee('Nick', 35)
employee.print_info()
employee.more_info()


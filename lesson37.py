# Конструктор класса - метод который вызывается при создании экземпляра касса

# Если в файле несколько классов и нужно импортировать конкретный
from classes import Person

# Импорт всех классов из файла classes
#import classes

person1 = Person('Sergey')
person1.print_info()                # Hello! My name is Sergey

person2 = Person('Andrey')
person2.print_info()                # Hello! My name is Andrey
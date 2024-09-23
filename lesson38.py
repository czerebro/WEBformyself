# Инкапсуляция - контроль доступа изменения объектов извне

from classes import Person

person1 = Person('Sergey')
person1.print_info()                # Name: Sergey. Age: 20. Age2: 30

person2 = Person('Andrey')
print(person2._age)                 # 20
#print(person2.__age)               # Выдаст ошибку
person2.print_info()                # Name: Andrey. Age: 20. Age2: 30
print(person2.get_age())            # 30
person2.set_age(50)
person2.print_info()                # Name: Andrey. Age: 20. Age2: 50
print(person2.age)                  # 50
person2.age = 35
person2.print_info()                # Name: Andrey. Age: 20. Age2: 35
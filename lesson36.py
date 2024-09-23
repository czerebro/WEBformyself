# Основы ООП. Класс и объект

# Объекты обладают свойстами - переменными и методами - функциями

class A:
    property = 'property'
    name = 'Sergey'

    def say_hi(self, name='Guest'):
        return 'Hi, ' + name

    def say_bye(self, name=''):
        if name:
            return 'Bye, ' + name
        else:
            return 'Bye, ' + self.name

a = A()
print(a)                        # <__main__.A object at 0x0000010E33C550D0>

# Создаём свойство вне класса
a.property1 = 'Property 1'
a.property2 = 'Property 2'
print(a.property1)              # Property 1

# Вызов метода
print(a.say_hi('John'))         # Hi, John
print(a.say_hi())               # Hi, Guest
print(a.say_bye())              # Bye, Sergey
print(a.say_bye('Andrey'))      # Bye, Andrey
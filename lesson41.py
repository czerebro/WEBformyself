# Полиморфизм

from classes import Person, Employee, Pupil

from classes import Person, Employee

person = Person('Kate', 18)
person.print_info()

pupil = Pupil('Nick', 35, 46)
pupil.print_info()
pupil.more_info()
print(pupil)
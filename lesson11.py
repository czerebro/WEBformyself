# Форматирование строк

name = 'John'
age = 30

print('My name is ' + name + '. I\'m ' + str(age))                          # My name is John. I'm 30
print('My name is %(x)s. I\'m %(y)d' %{'x': name, 'y': age})                # My name is John. I'm 30
print('My name is %s. I\'m %d' %(name, age))                                # My name is John. I'm 30
print('My name is %s. I\'m %d' %('David', age))                             # My name is David. I'm 30
print('Title: %s, Price: %f' %('Sony', 40))                                 # Title: Sony, Price: 40.000000
print('Title: %s, Price: %.2f' %('Sony', 40))                               # Title: Sony, Price: 40.00

# format
print('My name is {}. I\'m {}'.format(name, age))                           # My name is John. I'm 30
print('My name is {0}. I\'m {1}'.format(name, age))                         # My name is John. I'm 30 - номер позиции
print('My name is {x}. I\'m {y}'.format(x = name, y = age))                 # My name is John. I'm 30 - маркеры

# f-strings
print(f'My name is {name}. I\'m {age}')                                     # My name is John. I'm 30
print(f'My name is {name}. I\'m {age + 5}')                                 # My name is John. I'm 35
print('5 + 2 = {}'.format(5 + 2))                                           # 5 + 2 = 7
print(f'5 + 2 = {5 + 2}')                                                   # 5 + 2 = 7
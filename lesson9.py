# Операции со строками

# s1 = 'C:\d\new.txt'             # \n будет обработан как перенос строки
s2 = r'C:\d\new.txt'              # Сырая строка. Игнорируются управляющие последовательности

# Конкатенация строк

s3 = 'Py' 'thon'
print(s3)

s4 = 'Hello '
s5 = 'world!'
s6 = s4 + s5
print(s6)                          # Hello world!

name = 'Sergey'
age = 37
print('My name is ' + name)        # My name is Sergey
print('My name is ' + name + ". I'm " + str(age)) # My name is Sergey. I'm 37

# Индексация строк
'''
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9  10  11  12
  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1
'''
print(s6[0])                # H
print(s6[-1])               # !
print(s6[-12])              # H

# Срезы (последовательность символов)
# [X:Y:Z]
# X - начало среза
# Y - конец среза
# Z - шаг среза

print(s6[0:12])             # Hello world!
print(s6[0:20])             # Ошибки не будет. Выдаст: Hello world!
print(s6[15:20])            # Ошибки не будет. Выдаст пустую строку
print(s6[0:5])              # Hello
print(s6[:5])               # Hello
print(s6[6:])               # world!
print(s6[::])               # Hello world!
print(s6[::2])              # Hlowrd
print(s6[::-1])             #!dlrow olleH
print(s6[:5] + s6[6:])      # Helloworld!
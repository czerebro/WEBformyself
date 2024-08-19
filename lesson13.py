# Циклы for и while

# while True:
#     print('Hello')                  # Бесконечный цикл

i = 1

while i <= 10:
    print(i)
    i = i + 1                        # i += 1

print('Что хранится в i: ', i)       # 11

# Работа с функцией print
print('hello', 'world')              # hello world
print('hello', 'world', sep='!')     # hello!world
print('hello', 'world', end='^')     # hello world^
print('\n')

# for
s = 'Hello world'
for l in s:
    print(l, end=' ')

print('\n')

for l in s:
    if l == ' ':
        continue                    # Эта итерация пропускается и переходит к следующей
    print(l, end=' ')

print('\n')

for l in s:
    if l == ' ':
        break                       # Завершить цикл
    print(f"'{l}'", end=' ')

print('\n')

for l in 'Hello':
    if l == ' ':
        break                       # Завершить цикл
    print(f"'{l}'", end=' ')
else:
    print('No spaces')
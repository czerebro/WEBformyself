# Вывод таблицы умножения

for i in range(1, 11):
    for j in range(1, 6):
        print(f'{j} * {i} = {j * i}', end='\t\t')
        if j % 5 == 0:
            print(' ', end='\n')

print('\n')

for a in range(1, 11):
    for b in range(6, 11):
        print(f'{b} * {a} = {a * b}', end='\t\t')
        if b % 5 == 0:
            print(' ', end='\n')

# Вариант спикера
print('\nТаблица умножения')

for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t', end='')
    print('')
else:
    print('Well done')
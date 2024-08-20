# Списки = массивы

# Создание списков
l = [True, 1, 2, 3, ['test', 10.0], 'list']
l2 = list('hello')                              # функция list
l3 = list((1, 2, 3))                            # кортеж
l4 = [i for i in 'hello']                       # генератор списков
l5 = [i for i in 'hello world' if i != ' ']     # генератор с условием
l6 = [i for i in 'hello world' if i not in ['a', 'o', 'e']]
l7 = [i * 2 for i in 'hello']
l8 = list(range(10))
print(l8)

# Создание списка через генератор range()
print(type(range(3)))                           # <class 'range'>
print(list(range(3)))                           # [0, 1, 2]
print(list(range(1, 5)))                        # [1, 2, 3, 4]
print(list(range(0, 11, 2)))                    # [0, 2, 4, 6, 8, 10]


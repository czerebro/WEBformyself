# Лямбда-функции - анонимные функции. Содержат только одно выражение

def get_square(n):
    return n ** 2

print(get_square(5))

# Тоже самое через лямбда
get_square = lambda n: n ** 2
print(get_square(5))

# Ещё сократим
print((lambda n: n ** 2)(7))

# Пример 2
l = [1, 2, 3]

def get_double(l):
    return [i * 2 for i in l]

print(get_double(l))

# Через лямбда
def get_double2(l):
    return list(map(lambda n: n * 2, l))

print(get_double2(l))


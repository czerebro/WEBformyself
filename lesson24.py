# Методы для работы со словарями

product1 = {'title': 'Sony', 'price': 100}

# dict.clear() - очищает словарь
# dict.copy() - возвращает копию словаря
p = product1.copy()
print(p)                                # {'title': 'Sony', 'price': 100}

# dict.get(key[, default]) - возвращает значение ключа,
# но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
print(product1.get('title'))            # Sony

# dict.items() - возвращает пары (ключ, значение)
print(product1.items())                 # dict_items([('title', 'Sony'), ('price', 100)])

# dict.keys() - возвращает ключи в словаре
print(product1.keys())                  # dict_keys(['title', 'price'])

# dict.pop(key[, default]) - удаляет ключ и возвращает значение.
# Если ключа нет, возвращает default (по умолчанию бросает исключение)
print(product1.pop('title', 'NO'))      # Sony

# dict.popitem() - удаляет и возвращает пару (ключ, значение).
# Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены
print(product1.popitem())               # ('price', 100)


# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет,
# не бросает исключение, а создает ключ с значением default (по умолчанию None)
print(product1.setdefault('title2', 'test')) # test
print(product1)                         # {'title2': 'test'}

# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other.
# Существующие ключи перезаписываются. Возвращает None (не новый словарь!)
print(product1.update({'test': 'value'}))   # None
print(product1.update({'price': 200}))      # None
print(product1)                         # {'title2': 'test', 'test': 'value', 'price': 200}

# dict.values() - возвращает значения в словаре
print(product1.values())                # dict_values(['test', 'value', 200])

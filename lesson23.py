# Словари, асоциативные таблицы, хэш таблицы

# Создание словарей
d = {}                                          # Пустой словарь
print(type(d))                                  # <class 'dict'>
print(d)                                        # {}
product1 = {
    'title': 'Sony',
    'price': 100
}
print(product1)                                 # {'title': 'Sony', 'price': 100}

product2 = dict(title = 'iPhone', price = 100)  # Конструктор dict
print(product2)                                 #{'title': 'iPhone', 'price': 100}

# Создание словаря из вложенного списка
users = [
    ['bob@ya.ru', 'Bob'],
    ['kate@ya.ru', 'Kate'],
    ['john@ya.ru', 'John']
]
print(users)
d_users = dict(users)     # [['bob@ya.ru', 'Bob'], ['kate@ya.ru', 'Kate'], ['john@ya.ru', 'John']]
print(d_users)            # {'bob@ya.ru': 'Bob', 'kate@ya.ru': 'Kate', 'john@ya.ru': 'John'}

# Создание из кортежа
users_t = (
    ('bob@ya.ru', 'Bob'),
    ('kate@ya.ru', 'Kate'),
    ('john@ya.ru', 'John')
)
print(users_t)
t_users = dict(users_t)    # (('bob@ya.ru', 'Bob'), ('kate@ya.ru', 'Kate'), ('john@ya.ru', 'John'))
print(t_users)             # {'bob@ya.ru': 'Bob', 'kate@ya.ru': 'Kate', 'john@ya.ru': 'John'}

# Создание однотипного словаря
product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(product3)             # {'price1': 50, 'price2': 50, 'price3': 50}
product4 = dict.fromkeys(['price1', 'price2', 'price3'])
print(product4)             # {'price1': None, 'price2': None, 'price3': None}

# Генераторы
nums = {i: i + 1 for i in range(1, 10)}
print(nums)                 # {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

# Обращение к элементам словаря
print(product1['title'])
print(product1['price'])
print(nums[1])
print(product1.get('title'))
print(product1.get('title2', 'Такого ключа нет'))

# Перебрать словарь
for key in product1:
    print(key)                          # title и price

for key in product1:
    print(product1[key])                # Sony и 100

# items() - возвращает ключ значение
print(product1.items())                 # dict_items([('title', 'Sony'), ('price', 100)])
for key, value in product1.items():
    print(key, value)                   # title Sony и price 100

# Список словарей
products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 200},
    {'title': 'Samsung', 'price': 300}
]

print(products)                         # [{'title': 'Sony', 'price': 100}, {'title': 'iPhone', 'price': 200}, {'title': 'Samsung', 'price': 300}]

for product in products:
    print(product['title'], product['price']) # Sony 100
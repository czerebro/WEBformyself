# Регулярные выражения - модуль re

# https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F

# https://docs.python.org/3/library/re.html

import re

s = 'Это просто строка текста. А это ещё одна строка текста.'
pattern = 'строка'
print(s.find(pattern))                      # 11
print(pattern in s)                         # True

# re.search - возвращает объект соответствия
if re.search(pattern, s):
    print('Шаблон соответствует строке')
else:
    print('Подстрока не найдена')

match = re.search(pattern, s)
print(match)                                # <re.Match object; span=(11, 17), match='строка'>
print(match.span())                         # (11, 17)
print(match.start())                        # 11
print(match.end())                          # 17

# match() - ищет шаблон в начале строки
print(re.match(pattern, s))                 # None
print(re.match('Это', s))            # <re.Match object; span=(0, 3), match='Это'>
print(re.match('это', s))            # None - регистрозависимый

# findall() - ищет все совпадения во всей строке
print(re.findall(pattern, s))               # ['строка', 'строка']

# split() - разделение строки по шаблону
print(re.split('.', s))              # ['', '', '', '', '', '', '', '', '', '']
print(re.split('\.', s))             # ['Это просто строка текста', ' А это ещё одна строка текста', '']
print(re.split(r'\.', s))            # ['Это просто строка текста', ' А это ещё одна строка текста', '']
# Третий параметр это максимальное количество разделений начиная с нуля
print(re.split(r'\.', s, 1))  # ['Это просто строка текста', ' А это ещё одна строка текста.']

ss = '''Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, ٣, 0, 10
А это строка с разными символами: "!", "@", "-", "&", "?", "_"
a\\b\tc
test string'''

pattern2 = '\w'                             # Любой одинарный символ
pattern3 = '\w+'                            # + говорит что больше одного
pattern4 = r'[эт]'                          # Только буквы из квадратных скобок
pattern5 = r'[а-я]+'                        # Диапазон букв
pattern6 = r'[а-яА-Яё]+'                    # ё отдельная буква, диапазон маленьких и заглавных букв
pattern7 = r'[0-9]+'                        # только цифры
pattern8 = r'\d+'                           # только цифры со всех языков юникода
pattern9 = r'[\d-]'                         # цифры и символ -. - ставим в конце
pattern10 = r'a\\b\tc'                      # желательно использовать r чтобы найти экранирующие символы
pattern11 = r'\w+$'                         # слово с конца строки
pattern12 = r'^\w+'                         # слово с начала строки

print(re.findall(pattern2, ss))             # ['Э', 'т', 'о', 'п', 'р', 'о', 'с', 'т', 'о', 'с', 'т', 'р', 'о', 'к', 'а', 'т', 'е', 'к', 'с']
print(re.findall(pattern3, ss))             # ['Это', 'просто', 'строка', 'текста', 'А', 'это', 'ещё', 'одна', 'строка', 'текста']
print(re.findall(pattern4, ss))             # ['т', 'т', 'т', 'т', 'т', 'э', 'т', 'т', 'т', 'т', 'э', 'т', 'т', 'э', 'т', 'т']
print(re.findall(pattern5, ss))             # ['то', 'просто', 'строка', 'текста', 'это', 'ещ', 'одна', 'строка', 'текста', 'это', 'строка', 'с', 'цифрами', 'это', 'строка', 'с', 'разными', 'символами']
print(re.findall(pattern6, ss))             # ['Это', 'просто', 'строка', 'текста', 'А', 'это', 'ещё', 'одна', 'строка', 'текста', 'А', 'это', 'строка', 'с', 'цифрами', 'А', 'это', 'строка', 'с', 'разными', 'символами']
# флаг не зависимости от регистра
print(re.findall(pattern2, ss, flags=re.IGNORECASE))
print(re.findall(pattern7, ss))             # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '10']
print(re.findall(pattern8, ss))             # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '٣', '0', '10']
print(re.findall(pattern9, ss))             # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '٣', '0', '1', '0', '-']
print(re.findall(pattern10, ss))            # ['a\\b\tc']
print(re.findall(pattern11, ss))            # ['string']
print(re.findall(pattern12, ss))            # ['Это']

# Флаг ^ - начала текста
# Флаг $ - конец текста

email1 = 'mail@mail.ru'
email2 = 'mail@mail.com.ru'
email3 = 'mail@mail'


# Функция для валидации email

def validate_email(email):
    return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,3}$', email, re.IGNORECASE)  # валидация всей строки

print(validate_email(email1))               # <re.Match object; span=(0, 12), match='mail@mail.ru'>
print(validate_email(email2))               # <re.Match object; span=(0, 16), match='mail@mail.com.ru'>
print(validate_email(email3))               # None


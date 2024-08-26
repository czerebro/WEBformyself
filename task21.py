"""
Дан список words. Составьте из него список слов-палиндромов.
Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""
from pprint import pprint

#1
new_words = []
words = ['мадам', 'топот', 'test', 'madam', 'word']
for i in words:
    if i[::-1] == i:
        new_words.append(i)
print(new_words)

#1.1
words = ['мадам', 'топот', 'test', 'madam', 'word']
words2 = [i for i in words if i[::-1] == i]
print(words2)

#2
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
temp_str = [i for i in my_str if i.lower().split(' ')[::-1] != i.lower().split(' ')]
print(temp_str)

# Решение спикера

# Задача 1
#palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)

# Задача 1.1
# palindromes = [word for word in words if word == word[::-1]]
#
# print(palindromes)

# Задача 2
# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# palindromes = []
# for word in my_str:
#     word_r = word.replace(' ', '').lower()
#     if word_r == word_r[::-1]:
#         palindromes.append(word)
#
# print(palindromes)


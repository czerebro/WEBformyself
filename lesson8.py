# Строки

# https://proproprogs.ru/python_base/python3-specsimvoly-ekranirovanie-simvolov-raw-stroki

words1 = 'Hello world!'
print(words1)                           # Hello world!
words2 = "Hello world!"
print(words2)                           # Hello world!
words3 = "Helo 'world'!"
print(words3)                           # Helo 'world'!
words4 = "Hello \"test\" 'world'!"
print(words4)                           # Hello "test" 'world'!
words5 = "Hello \t 'world'!"
print(words5)                           # Hello 	 'world'!
words6 = "Hello \\t 'world'!"
print(words6)                           # Hello \t 'world'!

verse = 'Всё тихо - полная луна\n'\
         'Блестит меж встел над прудом,\n'\
         'И возле берега волна\n'\
         'С холодным резвится лучом.'

print(verse)

verse = ('Всё тихо - полная луна\n'
         'Блестит меж встел над прудом,\n'
         'И возле берега волна\n'
         'С холодным резвится лучом.')

print(verse)

verse = ('Всё тихо - полная луна\n\
Блестит меж встел над прудом,\n\
И возле берега волна\n\
С холодным резвится лучом.')

print(verse)

verse = '''\
         Всё тихо - полная луна
         Блестит меж встел над прудом,
         И возле берега волна
         С холодным резвится лучом.\
         '''

print(verse)

# вывести содержимое папки и каталогов в виде древа
"""
   walk хранит:
    Адрес очередного каталога в виде строки.
    В форме списка имена подкаталогов первого уровня вложенности для данного каталога.
    В виде списка имена файлов данного каталога.
"""

# https://pythoner.name/walk

import os

path = 'D:\\HONOR Share'

arr = list(os.walk(path))
print(list(arr))

def scan_folder(folder):
    # Распаковка кортежей
    for root, dirs, files in arr:
        # os.sep - Символ, используемый операционной системой для разделения имен компонентов.
        # Это '/' для POSIX и '\\' для Windows
        level_papki = root.count(os.sep)
        sdvig_papok = ' ' * 4 * level_papki
        sdvig_failov = ' ' * 4 * (level_papki + 1)
        # basename - обрезает путь и оставляет название папки
        print(f'{sdvig_papok}[{os.path.basename(root)}]')
        for file in files:
            print(f'{sdvig_failov}{file}')

scan_folder(path)
# Работа с файлами
# https://pythoner.name/file-io
# https://pythonz.net/references/named/open/

f = open('lesson33.txt', 'r', encoding='utf-8')
#text = f.read(1)
#text2 = f.read(8)
text = f.read()
print(f.encoding)
f.close()

print(text)
#print(text2)

# Дозапись в файл режим 'a'
ff = open('lesson33.txt', 'a', encoding='utf-8')
ff.write('Новая строка\n')
ff.close()

# Запись нескольких строк
lines = ['Новая строка 1', 'Новая строка 2']
fff = open('lesson33.txt', 'a', encoding='utf-8')
for i in lines:
    fff.write(i + '\n')
fff.writelines(lines)
fff.writelines(f'{i}\n' for i in lines)
fff.close()

# Чтение нескольких строк
f2 = open('lesson33.txt', 'r', encoding='utf-8')
for line in f2:
    print(line, end='')
f2.close()
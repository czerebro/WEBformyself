# Модуль ZipFile

# https://pythonworld.ru/moduli/modul-os-path.html

import zipfile, os

folder_path = 'C:\\AMD'
zip_path = 'C:\\AMD\\amd.zip'
zip_name = 'amd.zip'

# Создаём архив и открываем для записи
my_zip = zipfile.ZipFile(zip_path, 'w')

# Передаём то что хотим архивировать
my_zip.write('C:\\AMD\\dir1\\11.txt', compress_type=zipfile.ZIP_DEFLATED, arcname='имя_файла_в_ахиве.txt')

# Другой вариант записи
my_zip.write('C:\\AMD\\dir1\\11.txt', 'new.txt', compress_type=zipfile.ZIP_DEFLATED)

for folder, subfolders, files in os.walk(folder_path):
    print(folder, files)
    for file in files:
        if file == zip_name:
            continue
        #my_zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)
        my_zip.write(os.path.join(folder, file),
                     os.path.relpath(os.path.join(folder, file), folder_path),
                     compress_type=zipfile.ZIP_DEFLATED)

# Закрываем архив
my_zip.close()
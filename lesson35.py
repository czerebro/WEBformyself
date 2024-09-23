# Ошибки и исключения

# Отлавливаем конкретную ошибку
try:
    num = 100 / 0
except ZeroDivisionError:
    num = 0

print(num)                          # 0


# Отлавливаем любую ошибку
try:
    num = 100 / '2'
except Exception:
    num = 1

print(num)                          # 1


# Else and Finally
try:
    num = 100 / '2'
except Exception:
    num = 1
else:
    print('Else')                   # Выводится если код без ошибок
finally:
    print('Finaly')                 # Выводится в любом случае

print(num)                          # 1

while True:
    try:
        num = int(input('Введите число: '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('Число должно быть больше нуля')
    except ValueError:
        print('Нужно ввести числа не буквы')
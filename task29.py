"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd".
Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""

def odd_ball(arr):
    l = arr.index('odd')
    if arr.count(l):
        return True
    else:
        return False


def odd_ball(arr):
    return arr.index('odd') in arr


def odd_ball(arr):
    return bool([item for item in arr if item == arr.index('odd')])

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
print(odd_ball(["even",10,"odd",2,"even"])) # True


"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности 
включительно. Функция должна вернуть сумму всех чисел последовательности, 
кратных 3 или 5. Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""

def find_sum(n):
    res = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    print(res)


def find_sum2(n):
    print(sum(i for i in range(1, 1 + n) if i % 3 == 0 or i % 5 == 0))


find_sum(5) # return 8 (3 + 5)
find_sum(10) # return 33 (3 + 5 + 6 + 9 + 10)
find_sum2(5) # return 8 (3 + 5)
find_sum2(10)


"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]

def get_names(names):
    return [i for i in names if len(i) <= 4]


def get_names(names):
    [names.remove(name) for name in names if len(name) != 4]
    return names

print(get_names(names))
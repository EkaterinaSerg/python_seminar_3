# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите число N: '))
list_a = []
for n in range(n):
    num = int(input())
    list_a.append(num)
print(list_a)

x = int(input('Введите число x: '))
xmin = abs(x - list_a[0])
index = 0
for i in range(1, len(list_a)):
    count = abs(x - list_a[i])
    if count <= xmin:
        xmin = count
        index = i
print(f'Самое близкое число = {list_a[index]}')


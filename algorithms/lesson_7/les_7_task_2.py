'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

def merge_sort(arr, start, end):
    if end - start == 1:
        return
    elif end - start == 2:
        if arr[start] > arr[end - 1]:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]
        return
    delim = (start + end) // 2
    merge_sort(arr, start, delim)
    merge_sort(arr, delim, end)
    part1 = arr[start:delim]
    part2 = arr[delim:end]
    i1 = 0
    i2 = 0
    for i in range(start, end):
        if i2 == end - delim or (i1 < delim - start and part1[i1] < part2[i2]):
            arr[i] = part1[i1]
            i1 += 1
        else:
            arr[i] = part2[i2]
            i2 += 1
    return


array = [random.random() * (MAX_ITEM - MIN_ITEM) + MIN_ITEM for _ in range(SIZE)]
print(array)
sa = sorted(array)
merge_sort(array, 0, len(array))
print(array)
assert sa == array, 'Сортировка работает неверно'

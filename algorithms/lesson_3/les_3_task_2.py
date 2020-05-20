'''
Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив 
надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается 
с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
'''

from random import random

N = 10
arr = [0]*N
even = []

for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)

print(arr)
print('Индексы четных элементов: ', even)

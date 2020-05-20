'''
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

from random import random

N = 10
a = []
for i in range(N):
    a.append(int(random()*100))
    print(f'{a[i]}', end=' ')
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2,N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print(f'№ {min1+1} : {a[min1]}')
print(f'№ {min2+1} : {a[min2]}')

'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import random

N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i], end=' ')
print()
 
# 1-й вариант
# mn = min(arr)
# mx = max(arr)
# imn = arr.index(mn)
# imx = arr.index(mx)
# print(f'arr[{imn+1}]={mn} arr[{imx+1}]={mx}')
# arr[imn],arr[imx] = arr[imx],arr[imn]
 
# 2-й вариант (без использования встроенных функций)
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print(f'arr[{mn+1}]={arr[mn]} arr[{mx+1}]={arr[mx]}')
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b
 
for i in range(15):
    print(arr[i], end=' ')
print()

'''
Реализовать два небольших скрипта: 
а) бесконечный итератор, генерирующий целые числа, начиная с указанного, 
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. 
'''
from itertools import count, cycle


num = input('Введите два положительных целых числа через пробел, где второе больше первого: ').split()
for el in count(int(num[0])):
    try:
        if el > int(num[1]):
            break
        else:
            print(el)
    except:
        print('Ошибка ввода')
        break


my_list = ['one', 'two', 'tree', 'four', 'five']
iter = cycle(my_list)

for i in my_list:
    print(next(iter))

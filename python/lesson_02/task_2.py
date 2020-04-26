'''
Для списка реализовать обмен значений соседних элементов, 
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''
string = input('Введите через пробел несколько слов или цифр: ')
my_list = string.split(' ')
i = 0

if len(my_list) % 2 == 0:
    while i < my_list:
        element = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = element
        i += 2
else:
    while i < len(my_list)-1:
        element = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = element
        i += 2

print(my_list)

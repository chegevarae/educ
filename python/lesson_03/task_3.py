'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''
def my_fun(a, b, c):
    my_list = [a, b, c]
    my_list.pop(my_list.index(min(my_list)))
    print(my_list[0] + my_list[1])

my_fun(8, 4, 3)

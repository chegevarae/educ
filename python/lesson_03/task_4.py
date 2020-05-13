'''
Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора *. 
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
'''
# Внес исправления...
# Способ 1.
def my_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return 'Введено дробное число для отрицательной степени'
    return result
    
print(my_func(3, -3))


# Способ 2.
def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        result = x
        for _ in range(abs(y)-1):
            result *= x
        return f'{1/result:.5f}'
    except TypeError:
        return 'Ошибочное значение'
    
print(my_func2(3, -3))
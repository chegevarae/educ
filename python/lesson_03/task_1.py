'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def my_fun(a, b):
    return a / b

while True:
    numbers = input('Введите два числа через пробел: ').split()
    try:
        result = my_fun(float(numbers[0]), float(numbers[1]))
        print(f'Результат: {result:.3f}')
        break
    except:
        print('Деление на 0')

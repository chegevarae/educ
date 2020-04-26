'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой.
'''
class DivByZeroException(Exception):
    def __str__(self):
        return "Деление на ноль!"

    @staticmethod
    def division(num_1, num_2):
        if num_2 == 0:
            raise DivByZeroException()
        else:
            return num_1 / num_2

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

try:
    print(f'{num_1} / {num_2} = {DivByZeroException.division(num_1, num_2)}')
except DivByZeroException as err:
    print(err)

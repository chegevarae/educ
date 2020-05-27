'''
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Задача. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
'''

import cProfile
import math

# Вариант 1.
def sum1(n):
    e = 1
    s = 0
    for i in range(n):
        s += e
        e /= -2
    return s

# Вариант 2.
def sum2(n):
    e = 1
    lst = [1]
    for i in range(1,n):
        e /= -2
        lst.append(e)
    return sum(lst)

# Вариант 3.
def sum3(n):
    e = 1
    lst = [1]
    for i in range(1,n):
        e /= -2
        lst.append(e)
    return math.fsum(lst)


# sum1(4)
# sum2(4)
# sum3(4)


# АНАЛИЗИРУЕМ ФУНКЦИИ

# sum1()

# n = 10
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum1(10)"
# 1000 loops, best of 5: 1.98 usec per loop

# n = 100
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum1(100)"
# 1000 loops, best of 5: 14.3 usec per loop

# n = 1000
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum1(1000)"
# 1000 loops, best of 5: 156 usec per loop

# n = 10000
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum1(10000)"
# 1000 loops, best of 5: 1.64 msec per loop

# cProfile.run('sum1(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.017    0.017 <string>:1(<module>)
#         1    0.017    0.017    0.017    0.017 les_4_task_1.py:17(sum1)
#         1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# sum2()

# n = 10
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum2(10)"
# 1000 loops, best of 5: 2.84 usec per loop

# n = 100
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum2(100)"
# 1000 loops, best of 5: 24.1 usec per loop

# n = 1000
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum2(1000)"
# 1000 loops, best of 5: 234 usec per loop

# n = 10000
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum2(10000)"
# 1000 loops, best of 5: 2.41 msec per loop

# cProfile.run('sum2(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.063    0.063 <string>:1(<module>)
#         1    0.040    0.040    0.060    0.060 les_4_task_1.py:26(sum2)
#         1    0.000    0.000    0.063    0.063 {built-in method builtins.exec}
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.sum}
#     99999    0.018    0.000    0.018    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# sum3()

# n = 10
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum3(10)"
# 1000 loops, best of 5: 3.2 usec per loop

# n = 100
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum3(100)"
# 1000 loops, best of 5: 23.3 usec per loop

# n = 1000
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum3(1000)"
# 1000 loops, best of 5: 322 usec per loop

# n = 10000
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.sum3(10000)"
# 1000 loops, best of 5: 8.07 msec per loop

# cProfile.run('sum3(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.005    0.005    0.129    0.129 <string>:1(<module>)
#         1    0.044    0.044    0.124    0.124 les_4_task_1.py:35(sum3)
#         1    0.000    0.000    0.129    0.129 {built-in method builtins.exec}
#         1    0.062    0.062    0.062    0.062 {built-in method math.fsum}
#     99999    0.018    0.000    0.018    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ВЫВОД.
# Вариант 1 самый быстрый, т.к. не использует списки и встроенные функции.
# Далее идет вариант 2, т.к. он использует список + встроенную в Python функцию суммы.
# И самый последний вариант 3 самый медленный, т.к. он использует список + функцию суммы стороннего модуля math.

# Как видно из отчетов, использование списков значительно замедляет работу программы,
# помимо этого использование функций из сторонних модулей также ведет к замедлению вычислений.

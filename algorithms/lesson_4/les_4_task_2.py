'''
Написать два алгоритма нахождения i-го по счёту простого числа. 
Функция нахождения простого числа должна принимать на вход натуральное 
и возвращать соответствующее простое число. 
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''

import cProfile

# Функция определения простого числа с помощью алгоритма «Решето Эратосфена»
def IsSieve(n):
    sieve = [i for i in range(n+1)]
    sieve[1] = 0

    for i in range(2,n+1):
        if sieve[i]	!=	0:
            j = i * 2

            while j < n+1:
                sieve[j] = 0
                j += i

    if sieve[-1] != 0: 
        return True
    else:
        return False

# IsSieve(3)
# IsSieve(8)

# Функция определения простого числа без использования «Решета Эратосфена»
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

# IsPrime(3)
# IsPrime(8)


# АНАЛИЗИРУЕМ ФУНКЦИИ

# IsSieve()

# n = 10
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.IsSieve(10)"
# 1000 loops, best of 5: 5.29 usec per loop

# n = 100
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.IsSieve(100)"
# 1000 loops, best of 5: 46.4 usec per loop

# n = 1000
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.IsSieve(1000)"
# 1000 loops, best of 5: 683 usec per loop

# cProfile.run('IsSieve(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.112    0.112 <string>:1(<module>)
#         1    0.100    0.100    0.110    0.110 les_4_task_2.py:13(IsSieve)
#         1    0.010    0.010    0.010    0.010 les_4_task_2.py:14(<listcomp>)
#         1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# IsPrime()

# n = 10
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.IsPrime(10)"
# 1000 loops, best of 5: 332 nsec per loop

# n = 100
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.IsPrime(100)"
# 1000 loops, best of 5: 327 nsec per loop

# n = 1000
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.IsPrime(1000)"
# 1000 loops, best of 5: 326 nsec per loop

# cProfile.run('IsPrime(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:36(IsPrime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ВЫВОД.
# Вариант 1 самый долгий, т.к. использует список и его перебор для расчета простых чисел, 
# т.е. чем больше число передаваемого аргумента, тем дольше работает программа.
# Далее идет вариант 2, он самый быстрый поскольку не использует список.

# Как видно из отчетов, использование списка значительно замедляет работу программы,
# обычный перебор в цикле работает значительно быстрее, не увеличивая время работы программы.

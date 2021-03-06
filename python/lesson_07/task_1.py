'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86
	
3	5	32
2	4	6
-1	64	-8
	
3	5	8	3
8	3	7	1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. 
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки 
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
class Matrix():
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(str(s) for s in self.my_list)

    def __add__(self, other):
        return Matrix([[i[0] + i[1] for i in zip(j[0], j[1])] for j in zip(self.my_list, other.my_list)])

m1 = Matrix([[31, 22],[37,43],[51,86]])
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
m4 = Matrix([[-1, -2],[-2,2],[-1,4]])

print('m1:', m1, end = '\n\n', sep = '\n')
print('m2:', m2, end = '\n\n', sep = '\n')
print('m3:', m3, end = '\n\n', sep = '\n')
print('m4:', m4, end = '\n\n', sep = '\n')

print('m1 + m4:', m1 + m4, end = '\n\n', sep = '\n')

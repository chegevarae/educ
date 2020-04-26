'''
Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения 
и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры 
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''
class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imag * other.imag)

    def __str__(self):
        return f'({self.real}, {self.imag})'

c1 = Complex(1,2)
c2 = Complex(3,4)
print('c1 + c2 =', c1 + c2)
print('c1 * c2 =', c1 * c2)

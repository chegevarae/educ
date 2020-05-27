'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

import collections
from copy import deepcopy

hex_str = '0123456789ABCDEF'
hex_table = collections.defaultdict(int)
int_table = collections.defaultdict(int)
for i, item in enumerate(hex_str):
    hex_table[item] = i
    int_table[i] = item


class HexError(BaseException):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'Недопустимое значение: {self.num}'


class HexNum:
    h_table = hex_table
    i_table = int_table

    def __init__(self, num):
        try:
            self.num = collections.deque()
            for item in num:
                self.num.append(item.upper())
                if item.upper() not in self.h_table:
                    raise HexError(item)
        except TypeError:
            print('HexNum принимет только итерируемые объекты')

    def __str__(self):
        s = 'h_'
        for i in self.num:
            s += i
        return s

    def __add__(self, other):
        try:
            if len(other.num) > len(self.num):
                a = deepcopy(other.num)
                b = deepcopy(self.num)
            else:
                a = deepcopy(self.num)
                b = deepcopy(other.num)
        except AttributeError:
            print("Можно складывать только 16-е числа")
            raise SystemExit
        temp = 0
        result = collections.deque()
        for i in range(len(a)):
            first = self.h_table[a.pop()]
            if len(b) != 0:
                second = self.h_table[b.pop()]
            else:
                second = 0
            temp_res = first + second + temp
            if temp_res > 15:
                temp = 1
            else:
                temp = 0
            temp_res %= 16
            result.appendleft(self.i_table[temp_res])
        if temp != 0:
            result.appendleft(self.i_table[temp])
        result = HexNum(result)
        return result

    def __mul__(self, other):
        try:
            a = deepcopy(self.num)
            b = deepcopy(other.num)
        except AttributeError:
            print("Можно умножать только 16-е числа")
            raise SystemExit
        dec = 0
        answer = HexNum('0')
        result = collections.deque()
        for i in range(len(a) - 1, -1, -1):
            temp = 0
            for j in range(len(b) - 1, -1, -1):
                temp_res = self.h_table[a[i]] * self.h_table[b[j]] + temp
                if temp_res > 15:
                    temp = temp_res // 16
                else:
                    temp = 0
                temp_res = temp_res % 16
                result.appendleft(self.i_table[temp_res % 16])
            if temp != 0:
                result.appendleft(self.i_table[temp])
            for d in range(dec):
                result.append('0')
            result = HexNum(result)
            answer += result
            result = collections.deque()
            dec += 1
        return answer

    __rmul__ = __mul__


a = HexNum('a2')
b = HexNum('C4F')
c = HexNum('FA12C')
d = HexNum('39BD')
e = HexNum('FFF')
f = HexNum('FfF')
print(a + b)
print(a * b)
print(c * d)
print(e * f)

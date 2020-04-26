'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём 
оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных. 
'''
class Warehouse():
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        result = f'Состояние склада "{self.name}":\n'
        if self.items:
            for i, item in enumerate(self.items):
                result += f"{i+1}: {item}\n"
        else:
            result += 'Нет оборудования!\n'
        return result

    def debit(self, equipment):
        self.items.append(equipment)

    def _credit(self, equipment):
        if not equipment in self.items:
            raise KeyError(equipment)
        self.items.remove(equipment)

    def moveto(self, equipment, another_warehouse):
        self._credit(equipment)
        another_warehouse.debit(equipment)

class Equipment():
    def __init__(self, brand, model, price, weight):
        self.brand = brand
        self.model = model
        self.price = price
        self.weight = weight
        if not ((type(price) is int or type(price) is float) and price > 0):
            raise ValueError('Цена должна быть положительным числом!')
        if not ((type(weight) is int or type(weight) is float) and weight > 0):
            raise ValueError('Вес должен быть положительным числом!')

    def __str__(self):
        return f'{self.brand} {self.model} ценою {str(self.price)} руб. и весом {str(self.weight)} кг.'

class Printer(Equipment):
    itemname = 'Принтер'

class Scanner(Equipment):
    itemname = 'Сканер'

class Xerox(Equipment):
    itemname = 'Ксерокс'


e1 = Printer('Samsung', 'M2020W', 15450, 5.78)
print(e1)

e2 = Scanner('LG', 'LSM-100', 7500, 2.34)
print(e2)

e3 = Xerox('Xerox', 'phaser 3020', 37500, 19.10)
print(e3, '\n')

warehouse_main = Warehouse('Central')
warehouse_moscow = Warehouse('Moscow-Office')
warehouse_spb = Warehouse('StPetersburg-Office')

warehouse_main.debit(e1)
warehouse_main.debit(e2)
warehouse_main.debit(e3)
print(warehouse_main)

warehouse_main.moveto(e1, warehouse_moscow)
print(warehouse_main, 'Списано -', e1, '\n')
print(warehouse_moscow, 'Получено -', e1, '\n')

warehouse_main.moveto(e2, warehouse_moscow)
print(warehouse_main, 'Списано -', e2, '\n')
print(warehouse_moscow, 'Получено -', e2, '\n')

warehouse_main.moveto(e3, warehouse_spb)
print(warehouse_main, 'Списано -', e3, '\n')
print(warehouse_spb, 'Получено -', e3, '\n')

try:
    warehouse_main.moveto(e1, warehouse_spb)
except KeyError as err:
    print('Оборудование не найдено и не может быть списано!')

try:
    e4 = Xerox('Xerox', 'SXD55', -45632, -12.46)
    print(e4)
except ValueError as err:
    print(err)

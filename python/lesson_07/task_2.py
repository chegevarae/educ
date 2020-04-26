'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothing(ABC):
    name = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod 
    def fabric_consumption(self):
        pass

class Coat(Clothing):
    name = 'пальто'

    def __init__(self, v):
        self.v = v

    def __str__(self):
        return '[' + self.name + ' размера ' + str(self.v) + ']'

    @property
    def fabric_consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothing):
    name = 'костюм'

    def __init__(self, h):
        self.h = h

    def __str__(self):
        return '[' + self.name + ' размера ' + str(self.h) + ']'

    @property
    def fabric_consumption(self):
        return 2 * self.h + 0.3


coat = Coat(52)
print(coat, '; необходимо ткани:', coat.fabric_consumption)

suit = Suit(50)
print(suit, '; необходимо ткани:', suit.fabric_consumption)

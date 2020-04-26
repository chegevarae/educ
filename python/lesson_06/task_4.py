'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую 
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение 
о превышении скорости. 
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
выведите результат. Выполните вызов методов и также покажите результат. 
'''
import random

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self):
        turn = random.choice(['направо', 'налево'])
        return f'Машина повернула {turn}'

    def show_speed(self):
        current_speed = random.randint(0,180)
        return f'Текущая скорость {current_speed}'

class TownCar(Car):
    def show_speed(self):
        current_speed = random.randint(0,180)
        print(f'Текущая скорость {current_speed}')
        if current_speed > 60:
            print('Внимание! Превышение скорости')

class SportCar(Car):
    def sport(self):
        return 'Это спорткар!'

class WorkCar(Car):
    def show_speed(self):
        current_speed = random.randint(0,180)
        print(f'Текущая скорость {current_speed}')
        if current_speed > 40:
            print('Внимание! Превышение скорости')

class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            return 'Внимание! Это полиция'
        else:
            return 'Это похожая на полицию машина'


a = Car(90, 'Red', 'Mazda', False)
print(a.name, a.color)
print(a.go())
print(a.turn())
print(a.show_speed())
print('-----------')
b = PoliceCar(100, 'Blue', 'BMW', True)
print(b.name, b.color)
print(b.go())
print(b.turn())
print(b.show_speed())
print(b.police())
print('-----------')

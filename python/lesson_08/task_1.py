'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату 
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год 
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
'''
import re

class MyDate():
    def __init__(self, datestr):
        dayto, monthto, yearto = self.parse_datestr(datestr)
        if MyDate.verify_ymd(dayto, monthto, yearto):
            self.dayto = dayto
            self.monthto = monthto
            self.yearto = yearto

    def __str__(self):
        return "MyDate(%02d-%02d-%04d)" % (self.dayto, self.monthto, self.yearto)

    @classmethod
    def parse_datestr(cls, datestr):
        match = re.match(r'(\d{2})-(\d{2})-(\d{4})', datestr)
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            raise ValueError("Введенная дата " + datestr + " не соответствует формату DD-MM-YYYY")

    @staticmethod
    def verify_ymd(dayto, monthto, yearto):
        if not(yearto >= 0 and yearto <= 2999):
            raise ValueError( "Некорректный год: " + str(yearto))
        if not(monthto >= 1 and monthto <= 12):
            raise ValueError("Некорректный месяц: " + str(monthto))
        if not(dayto >= 1 and dayto <= 31):
            raise ValueError("Некорректный день: " + str(dayto))
        return True

try:
    d = MyDate('21-10-2019')
    print(d)
except Exception as err:
    print(err)

try:
    d = MyDate('35-10-2019')
    print(d)    
except Exception as err:
    print(err)

try:    
    d = MyDate('12-20-2019')
    print(d)
except Exception as err:
    print(err)

try:    
    d = MyDate('12-20-3540')
    print(d)
except Exception as err:
    print(err)

try:    
    d = MyDate('12-TXT-2019')
    print(d)
except Exception as err:
    print(err)

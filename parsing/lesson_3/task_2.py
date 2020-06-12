'''
Написать функцию, которая производит поиск и выводит на экран 
вакансии с заработной платой больше введенной суммы.
'''

from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['hh_vac']


def search_vac(min_salary, max_salary, currency):
    if max_salary == 0:
        return [pprint(el) for el in db.vac.find({'$and': [{'min_salary': {'$gte': min_salary}}, {'currency': f'{currency}'}]})]
    else:
        obj = {}
        obj = [el for el in db.vac.find({'$and': [{'$and': [{'min_salary': {'$gte': min_salary}}, {'min_salary': {'$lte': max_salary}}]}, {'$and': [{'max_salary': {'$gte': min_salary}}, {'max_salary': {'$lte': max_salary}}]}, {'currency': f'{currency}'}]})]
        return [pprint(db.vac.find_one(el)) for el in obj]


salary = []
salary = input('Введите через пробел размер з/п (от до) или просто (от): ').split()
currency = input('Введите наименование валюты (USD,EUR,KZT,руб. и т.п., как на hh.ru): ')

if len(salary) > 0 and len(salary) < 3:
    if len(salary) == 2 and salary[0].isdigit() == True and salary[1].isdigit() == True:
        min_salary = int(salary[0])
        max_salary = int(salary[1])
    elif len(salary) == 1 and salary[0].isdigit() == True:
        min_salary = int(salary[0])
        max_salary = int(0)
    search_vac(min_salary, max_salary, currency)
else:
    print('Неверный ввод!')

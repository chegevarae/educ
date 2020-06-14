'''
Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB 
и реализовать функцию, записывающую собранные вакансии в созданную БД.
'''

from bs4 import BeautifulSoup as bs
import requests, re
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['hh_vac']


# https://hh.ru/search/vacancy?text=Data+scientist
main_link = 'https://hh.ru'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

page = 0
vacname = 'Data+scientist'


while True:
    response = requests.get(main_link + '/search/vacancy?text=' + vacname + '&page=' + str(page), headers=headers)
    soup = bs(response.text, 'lxml')
    el = len(soup.findAll('div', {'class':'vacancy-serp-item'}))
    if el == 0: # Проверка следующей страницы, если ее нет, то break
        break

    for i in range(el):
        try:
            tmp = {}
            vacancy = soup.findAll('div', {'class':'vacancy-serp-item'})[i]

            tmp['name'] = vacancy.find('a', {'class':'bloko-link'}).getText().strip()
            link = vacancy.find('a', {'class':'bloko-link'})['href'].strip()
            tmp['link'] = re.sub('(?i)\?.*?$', '', link)
            tmp['company'] = vacancy.find('a', {'class':'bloko-link bloko-link_secondary'}).getText().strip()
            salary = vacancy.find('div', {'class':'vacancy-serp-item__sidebar'}).getText().strip()
            if len(salary) != 0:
                currency = re.search('(?i)[A-zА-я\.]+\s[A-zА-я\.]+$|[A-zА-я\.]+$', salary).group(0)
                _sal = salary.split('-')
                if len(_sal) == 1:
                    if 'от' in _sal[0]:
                        min_salary = int(re.sub('\D', '', _sal[0]))
                        max_salary = int(0)
                    else:
                        max_salary = int(re.sub('\D', '', _sal[0]))
                        min_salary = int(0)
                else:
                    min_salary = int(re.sub('\D', '', _sal[0]))
                    max_salary = int(re.sub('\D', '', _sal[1]))
            else:
                min_salary, max_salary = int(0), int(0)
                currency = None

            tmp['min_salary'] = min_salary
            tmp['max_salary'] = max_salary
            tmp['currency'] = currency

            db.vac.insert_one(tmp) # Запись вакансии в БД

        except AttributeError as e:
            print('AttributeError:', e)
            continue
        except Exception as e:
            print('Error:', e)
            continue      

    page += 1
    print('page', page) 

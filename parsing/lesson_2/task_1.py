'''
Необходимо собрать информацию о вакансиях на вводимую должность 
(используем input или через аргументы) с сайта superjob.ru и hh.ru. 
Приложение должно анализировать несколько страниц сайта
(также вводим через input или аргументы). 
Получившийся список должен содержать в себе минимум:
    *Наименование вакансии
    *Предлагаемую зарплату (отдельно мин. и отдельно макс.)
    *Ссылку на саму вакансию        
    *Сайт откуда собрана вакансия
По своему желанию можно добавить еще работодателя и расположение. 
Данная структура должна быть одинаковая для вакансий с обоих сайтов. 
Общий результат можно вывести с помощью dataFrame через pandas.
'''

from bs4 import BeautifulSoup as bs
import requests, re
from pprint import pprint
import time, csv

# https://hh.ru/search/vacancy?text=Data+scientist
main_link = 'https://hh.ru'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

page = 0
vacancies = []
vacname = 'Data+scientist'

with open('hh.csv', 'w', newline='', encoding='utf-8') as f:
    columns = ['name', 'link', 'company', 'salary']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()


while True:
    response = requests.get(main_link + '/search/vacancy?text=' + vacname + '&page=' + str(page), headers=headers)
    soup = bs(response.text, 'lxml')
    el = len(soup.findAll('div', {'class':'vacancy-serp-item'}))
    if el == 0:
        break

    for i in range(el):
        try:
            spam = []
            vacancy = soup.findAll('div', {'class':'vacancy-serp-item'})[i]

            spam.append(vacancy.find('a', {'class':'bloko-link'}).getText().strip())
            spam.append(vacancy.find('a', {'class':'bloko-link'})['href'].strip())
            spam.append(vacancy.find('a', {'class':'bloko-link bloko-link_secondary'}).getText().strip())
            salary = vacancy.find('span', {'data-qa':'vacancy-serp__vacancy-compensation'})
            if salary:
                spam.append(salary.getText().strip())

            vacancies.append(spam)

        except AttributeError as e:
            print('AttributeError:', e)
            continue
        except Exception as e:
            print('Неизвестная ошибка', e)
            continue      

    page += 1
    print('page', page) 


time.sleep(2)
with open('hh.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(vacancies)

'''
Написать программу, которая собирает входящие письма из своего 
или тестового почтового ящика и сложить данные о письмах в базу данных. 
* от кого, 
* дата отправки, 
* тема письма, 
* текст письма полный
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import time, re

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['mailru_letters']

driver = webdriver.Chrome()

# При необходимости максимизируем окно браузера
# driver.maximize_window()

# Получаем страницу
driver.get('https://account.mail.ru/login')
time.sleep(5)

# Проверяем куда попали
assert "Авторизация" in driver.title

# Вводим логин
elem = driver.find_element_by_name('username')
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.RETURN)
time.sleep(2)

# Вводим пароль
elem = driver.find_element_by_name('password')
elem.send_keys('NextPassword172')
elem.send_keys(Keys.RETURN)
print('Ожидаем загрузки страницы...')
time.sleep(30)

# Проверяем куда попали
assert "Входящие" in driver.title

# Прокручиваем страницу и парсим письма
lst = []
for i in range(40):
    letter = driver.find_elements_by_class_name('llc')
    actions = ActionChains(driver)
    actions.move_to_element(letter[-1])
    actions.perform()

    blocks = driver.find_elements_by_css_selector("a.llc") # "s" на конце для получения списка!
    print(f'Найдено писем: {len(blocks)}')
    for block in blocks:
        try:
            tmp = {}
            tmp['corresp'] = block.find_element_by_css_selector("span.ll-crpt").text
            tmp['subject'] = block.find_element_by_css_selector("span.ll-sj__normal").text
            textletter = block.find_element_by_css_selector("span.ll-sp__normal").text
            tmp['textletter'] = re.sub('\.+', '', textletter)
            tmp['dateletter'] = block.find_element_by_css_selector("div.llc__item_date").text

            lst.append(tmp)

        except Exception as e:
            print('Error:', e)
            continue

    print(f'Прокручено писем: {i}0')
    time.sleep(0.5)

db.letters.insert_many(lst)
print('Процесс завершен!')

# Не успел реализовать очистку дублей, позже доделаю!

'''
Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД. 
Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['ulmart']

driver = webdriver.Chrome()

# При необходимости максимизируем окно браузера
# driver.maximize_window()

# Создаем ссылку и делаем запрос
main_link = 'https://www.ulmart.ru'
driver.get(main_link + '/catalog/brand_computers')

# Истек сертификат, кликаем по кнопкам, чтобы зайти на сайт
button = driver.find_element_by_id('details-button')
button.click()
button = driver.find_element_by_id('proceed-link')
button.click()

# Подтверждаем свой город
button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'cityOk'))
    )
button.click()

# Кликаем в цикле по кнопке: "Показать еще"
while True:
    try:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-product-more'))
        )
        button.click()
        time.sleep(5)
    except:
        break

# Парсим элементы и записываем их в базу
blocks = driver.find_elements_by_css_selector("div.b-product__center") # "s" на конце для получения списка!
print(f'Блоков: {len(blocks)}')
for block in blocks:
    try:
        tmp = {}
        tmp['title'] = block.find_element_by_class_name("must_be_href").text
        tmp['link'] = block.find_element_by_class_name("must_be_href").get_attribute("href")
        tmp['descr'] = block.find_element_by_css_selector("div.b-product__descr").text
        tmp['SKU'] = block.find_element_by_css_selector("span.num").text

        db.computers.insert_one(tmp)

    except Exception as e:
        print('Error:', e)
        continue

print('Парсинг завершен!')

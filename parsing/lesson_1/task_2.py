'''
Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). 
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
'''

import requests

main_link = 'https://api.anti-captcha.com/getBalance'
params = {'clientKey': '1234567'}
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

response = requests.get(main_link,params=params, headers=headers)

print(response.text)

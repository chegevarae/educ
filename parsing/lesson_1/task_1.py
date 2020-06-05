'''
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев 
для конкретного пользователя, сохранить JSON-вывод в файле *.json
'''

import requests

with open('result.json', 'w', encoding='utf-8') as f:
    rep = requests.get('https://api.github.com/users/sever-ip/repos')
    f.write(rep.text)

# Запросы друзей и подписчиков из БД по user_id

from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['insta']

# Получаем всех подписчиков пользователя
followers = db.followers.find({"user_id": "38408344862"})
for item in followers:
    print(item)

print('*' * 100)

# Получаем все подписки пользователя
follow = db.follow.find({"user_id": "38408344862"})
for item in follow:
    print(item)

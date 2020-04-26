'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''
def my_fun(name, surname, age, city, email, phone):
    print(f"name - {name}; surname - {surname}; age - {age}; city - {city}; email - {email}; phone - {phone}")

my_fun(name='Name', surname='Surname', age='1977', city='Moscow', email='test@test.ru', phone='79991234567')

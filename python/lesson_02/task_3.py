'''
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict. 
'''
# list
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
while True:
    number = int(input("Введите порядковый номер месяца в виде целого числа от 1 до 12: "))
    if number >= 1 and number <= 12:
        if number >= 3 and number <= 5:
            print(f'Введенный месяц {number} - это {season_list[1]}!')
        elif number >= 6 and number <= 8:
            print(f'Введенный месяц {number} - это {season_list[2]}!')
        elif number >= 9 and number <= 11:
            print(f'Введенный месяц {number} - это {season_list[3]}!')
        else:
            print(f'Введенный месяц {number} - это {season_list[0]}!')
        break

# dict
season_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
while True:
    number = int(input("Введите порядковый номер месяца в виде целого числа от 1 до 12: "))
    if number >= 1 and number <= 12:
        if number >= 3 and number <= 5:
            print(f'Введенный месяц {number} - это {season_dict.get(2)}!')
        elif number >= 6 and number <= 8:
            print(f'Введенный месяц {number} - это {season_dict.get(3)}!')
        elif number >= 9 and number <= 11:
            print(f'Введенный месяц {number} - это {season_dict.get(4)}!')
        else:
            print(f'Введенный месяц {number} - это {season_dict.get(1)}!')
        break

'''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''
seconds = int(input('Введите любое количество секунд: ')) 

hours = seconds // 3600
residue = seconds % 3600
minutes = residue // 60
seconds = residue % 60

print('%d:%d:%d' %(hours, minutes, seconds))

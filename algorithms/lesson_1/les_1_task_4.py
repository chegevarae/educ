'''
Пользователь вводит две буквы. Определить, на каких местах 
алфавита они стоят, и сколько между ними находится букв.
'''

a = input('Введите первую букву в диапазоне от "a" до "z": ')
b = input('Введите вторую букву в диапазоне от "a" до "z": ')

a1 = ord(a) - ord('a') + 1
b1 = ord(b) - ord('a') + 1

print(f'Позиция "{a}" равна {a1}, позиция "{b}" равна {b1}')
print(f'Кол-во символов между буквами равно: {abs(a1-b1)-1}')

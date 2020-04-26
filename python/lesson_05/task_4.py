'''
Создать (не программно) текстовый файл со следующим содержимым: 
One - 1
Two - 2
Three - 3
Four - 4
Необходимо написать программу, открывающую файл на чтение 
и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл. 
'''
import os
if os.path.exists('task_4_2_file.txt') == True:
    os.remove('task_4_2_file.txt')

dict_ = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task_4_2_file.txt', 'a', encoding='utf-8') as f2:
    with open('task_4_file.txt', 'r', encoding='utf-8') as f:
        list_ = f.read().split('\n')
        list_.pop(4)
        for i in list_:
            i = i.split(' - ')
            f2.writelines(dict_[i[0]] + ' - ' + i[1] + '\n')

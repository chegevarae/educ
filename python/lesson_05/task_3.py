'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''
f = open('task_3_file.txt', encoding='utf-8')

my_list = f.readlines()
salary = 0

for i in my_list:
    ls = i.split()
    if salary == 0:
        salary = int(ls[1])
    else:
        salary = salary + int(ls[1])
    if int(ls[1]) < 20000:
        print(f'{ls[0]} имеет оклад меньше 20000')

print('Средний доход сотрудников составляет:', salary/len(my_list))

f.close()

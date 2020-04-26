'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('task_2_file.txt', 'w', encoding='utf-8') as f:
    my_list = ['Я помню чудное мгновенье:', 'Передо мной явилась ты,', 'Как мимолетное виденье,', 'Как гений чистой красоты.']
    for i in my_list:
        f.write(i + '\n')

f = open('task_2_file.txt')

my_list = []
for i in f: 
    my_list.append(len([len(i) for x in i.split()]))
print('Кол-во строк:', len(my_list))

for i in range(len(my_list)):
    print(f'{i+1} строка: {my_list[i]} слова')

f.close()

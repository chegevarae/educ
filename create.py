# Быстрое создание папок и файлов для выполнения ДЗ
import os

path_dir = os.getcwd()
print('Текущая директория:', path_dir)
print('Список папок и файлов:', os.listdir(), '\n')

folder = input('Ввести название папки-репозитория (Exit -> Enter): ')
select = input('Ввести название папки для ДЗ (Exit -> Enter): ')
flist = input('Ввести через пробел название файла и кол-во файлов для создания, например: "les_1_task 5" (Exit -> Enter): ').split()

while True:
    try:
        if folder != '' and select != '' and flist != '':
            dir_puth = os.path.join(path_dir, folder, select)
            if os.path.exists(dir_puth) == False:
                os.makedirs(dir_puth)
            for i in list(range(1, int(flist[1])+1)):
                fname = flist[0] + '_' + str(i) + '.py'
                fpath = os.path.join(dir_puth, fname)
                with open(fpath, 'w', encoding='utf-8') as f:
                    for i in range(3):
                        if i == 1: f.write(fname + '\n')
                        else: f.write("'''\n")
        else: break
    except:
        print('Ошибка ввода!')

'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор. 
'''
result = [el for el in list(range(3, 9)) if list(range(3, 9)).count(el) == 1]
print(result)
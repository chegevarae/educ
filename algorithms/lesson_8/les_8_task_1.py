'''
На улице встретились N друзей. Каждый пожал руку всем остальным 
друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

# Вариант 1
n = int(input('Введите количество друзей: '))
print('Строим ориентированный граф:')
graph = [] 
graph = [[0] * i + [0] + [1] * (n - i - 1) for i in range(n)]
print(*graph, sep='\n')

r = 0
for i in graph:
    r += sum(i)

print(f'Количество рукопожатий равно {r}')


# Вариант 2
def friends(num):
    if num < 2:
        return 'Слишком мало друзей'

    graph = []

    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))

    print(graph)
    return len(graph) // 2

print(friends(int(input('Сколько друзей встретилось: '))))

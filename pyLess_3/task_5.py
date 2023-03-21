'''
*****(4)Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
 сформированную из отсортированных в лексикографическом порядке параметров.

Пример:

Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:

challenge=17&course=python&lesson=2
'''

def query(data):
    resStr = ''
    for i in list(sorted(data, key = lambda x = data.keys() : (x, [i for i in map(ord, x)]))):
        resStr += f'{i}={data[i]}&'
    return resStr[:-1]

print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))
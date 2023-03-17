'''На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые
нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть'''

'''Примем за 0 - орел, за 1 - решку'''

import random # импорт модуля для генерации случайных значений 0 или 1
sideCoinList = [] #создаем список для хранения значений сторон монет

while True: # запускае бесконечный цикл
    countSCL = input('Enter count coints: ') # просим пользователя ввести длину списка
    if countSCL.isdigit() & countSCL.isdigit() > 0: # проверяем что значение является числом
        countSCL = int(countSCL) # переводим значение в целочисленный тип
        break # останавливаем цикл
    else:
        print("Enter error! Try again!")

cntsChangeCoin = {'eagle' : 0, 'tail' : 0} # словарь для подсчета количества сторон
for i in range(countSCL): # цикл для прохода по длине списка
    randSide = random.randint(0, 1) # генерируем значение для очередного шага добавления в список
    sideCoinList.append(randSide) # добавляем очередное значение в список
    '''Т.к задача учебная позволю себе произвести подсчет переворотов монет прям в этом цикле =)'''
    if randSide == 0:
        cntsChangeCoin['eagle'] += 1
    else:
        cntsChangeCoin['tail'] += 1

print(sideCoinList) # распечатываем список
print(cntsChangeCoin)
print(f'Minimal need count change side coin:'
      f' {min(cntsChangeCoin.values())}, side coin:'
      f' {next(ch for ch, code in cntsChangeCoin.items() if code == min(cntsChangeCoin.values()))}')

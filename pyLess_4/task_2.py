'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
'''

import numpy as np

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def createArrays() -> np.array:
    while True:
        countBush = checkInput(f"Enter count bush: ")
        if countBush < 3:
            print("Error! Can't be less than 3 bushes!")
        else:
            bushArr = np.array([0] * countBush)

            for i in range(len(bushArr)):
                bushArr[i] = checkInput(f"Enter count berries {i + 1} bush: ")
            break

    return bushArr

def resultSum() -> int:
    a = createArrays()
    maxSum, nextSum = 0, 0
    for i in range(len(a)):
        nextSum += a[i - 2] + a[i - 1] + a[i]
        if maxSum < nextSum:
            maxSum = nextSum
        nextSum = 0
    return maxSum

print(resultSum())


'''a = [13, 14, 1, 4, 5, 7, 9, 10]

maxSum = 0
nextSum = 0

for i in range(len(a)):
    if i > len(a):
        print(a[i - 2], a[i - 1], a[i])
        i -= len(a)
    else:
        print(a[i-2], a[i-1], a[i])
        nextSum += a[i-2] + a[i-1] + a[i]
        if maxSum < nextSum:
            maxSum = nextSum

        nextSum = 0

print(maxSum)'''



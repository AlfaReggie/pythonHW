'''Требуется найти в массиве A[1..N] самый близкий по величине
элемент к заданному числу X. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    6
    -> 5'''

import numpy as np

def checkInput(text):
    while True:
        nmbr = input(text)
        try:
            return int(nmbr)
        except:
            return "Enter error!"

def createArray():
    while True:
        N = checkInput('Enter count elements in array: ')
        if N > 0:
            arrList = [(i + 1) for i in range(N)]
            return np.array(arrList)
        else:
            continue

def checkCount():
    resArray = createArray()
    print(resArray)
    X = checkInput('Enter the number you need: ')
    if X in resArray:
        return X
    else:
        if X < resArray[0]:
            return resArray[0]
        else:
            return resArray[-1]

print(checkCount())
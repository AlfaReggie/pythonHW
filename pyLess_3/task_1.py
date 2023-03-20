'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
    '''
import numpy as np

def checkInput(massege):
    while True:
        nmbr = input(massege)
        if nmbr.isdigit():
            return int(nmbr)
        else:
            print("Enter error!")

def createArray():
    N = checkInput('Enter count elements in array: ')
    arrList = [(i + 1) for i in range(N)]
    return np.array(arrList)

def checkCount():
    resArray = createArray()
    X = checkInput('Enter the number you need: ')
    count = 0
    for i in resArray:
        if i == X:
            count += 1
    return count

print(checkCount())
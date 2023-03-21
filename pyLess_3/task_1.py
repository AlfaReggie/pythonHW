"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
1 2 3 4 5
3
-> 1
"""

import numpy as np

def checkInput(text):
    while True:
        nmbr = input(text)
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
    print(resArray)
    X = checkInput('Enter the number you need: ')
    count = 1
    if len(resArray) <= 9:
        return 1
    else:
        resArray = resArray[9:]
        for i in resArray:
            numb = i
            while numb != 0:
                nxtDig = numb % 10
                if nxtDig == X:
                    count += 1
                numb //= 10
    return count

print(checkCount())



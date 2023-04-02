'''
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19]
'''
import numpy as np

def checkInput(message: str) -> str:
    userInp = input(message)
    if userInp == 'q' or userInp.replace("-", '').isdigit():
        return userInp
    else:
        print("Error!")
        return checkInput(message)

def createArr(usrArr):
    nxtEl = checkInput('Enter next element array: ')
    if nxtEl == "q":
        return usrArr
    usrArr.append(int(nxtEl))
    return createArr(usrArr)

a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
a_idx = []
def findIdxEl(a, a_idx, Min, Max):
    if 

'''userArray = []
print(createArr(userArray))'''
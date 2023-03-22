'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''

import numpy as np

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def createArrays(sizeDict: dict, listArray: list) -> list:
    for key in sizeDict.keys():
        while True:
            sizeInp = checkInput(f"Enter size {key} set: ")
            if sizeInp < 1:
                print("Error! Size array can't less one!")
            else:
                sizeDict[key] = sizeInp
                listArray.append(np.array([0] * sizeInp))
                break
    for i in range(len(listArray)):
        countArr = 0
        while countArr < len(listArray[i]):
            listArray[i][countArr] = checkInput(f"Enter {countArr + 1}"
                                               f" element {i + 1} array: ")
            countArr += 1

    return listArray

def resultSet() -> set:
    sizeDict = {"n": 0, "m": 0}
    listArr = []
    arrsList = createArrays(sizeDict, listArr)
    print(f'1 array: {arrsList[0]}, 2 array: {arrsList[1]}')

    return f"result: {sorted(set(arrsList[0]) & set(arrsList[1]))}"


print(resultSet())






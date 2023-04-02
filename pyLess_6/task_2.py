'''
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19]
'''

import numpy as np

def checkInput(message: str, flag: str) -> str:
    userInp = input(message)
    if flag == 'arFlag':
        if userInp == 'q' or userInp.replace("-", '').isdigit():
            return userInp
        else:
            print("Error!")
            return checkInput(message, 'arFlag')
    if flag == 'rangeFlag':
        if userInp.replace("-", '').isdigit():
            return userInp
        else:
            print("Error!")
            return checkInput(message, 'rangeFlag')

def createArr(usrArr):
    nxtEl = checkInput('Enter next element array: ', 'arFlag')
    if nxtEl == "q":
        return usrArr
    usrArr.append(int(nxtEl))
    return createArr(usrArr)

def findIdxEl(a, a_idx, min_el, max_el, i):
    if i >= len(a):
        return a_idx
    if min_el <= a[i] <= max_el:
        a_idx.append(i)
    return findIdxEl(a, a_idx, min_el, max_el, i + 1)

def main() -> list:
    usArr = createArr([])
    rangeDict = {'minEl': 0, 'maxEl': 0}
    for i in rangeDict.keys():
        rangeDict[i] = int(checkInput(f'Enter {i} range: ', 'rangeFlag'))
    resArr = findIdxEl(usArr, [], rangeDict['minEl'], rangeDict['maxEl'], 0)
    print(resArr)


if __name__ == "__main__":
    main()
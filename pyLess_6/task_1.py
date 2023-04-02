'''
Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def myFanc(a_1, d, cnt, j) -> str:
    if j != 0:
        return a_1
    res = []
    for i in range(1, cnt + 1):
        res.append(myFanc(a_1 + (i - 1) * d, d, cnt, j + 1))
    return res

def funcCreateVariabl() -> int:
    hlpLst = ['first element', 'difference', 'length array']
    valList = []
    for i in range(len(hlpLst)):
        if i < 2:
            nxtVal = checkInput(f'Enter {hlpLst[i]}: ')
            valList.append(nxtVal)
        elif i == 2:
            while True:
                nxtVal = checkInput(f'Enter {hlpLst[i]}: ')
                if nxtVal < 0:
                    print("Error! Can't negative!")
                else:
                    valList.append(nxtVal)
                    break
    return myFanc(valList[0], valList[1], valList[2], 0)

print(funcCreateVariabl())
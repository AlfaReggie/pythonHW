'''
Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел,
 сумма цифр которых равна s. Запись натурального числа не может начинаться с цифры 0.
В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.
3 15 -> 69
4 16 -> 564
2 3 -> 3
6, 40 ->10746
'''

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def funcCreateVariabl() -> int:
    usDict = {'k': 0, 's': 0}
    for i in usDict.keys():
        while True:
            nxtVar = checkInput(f'Enter {i}: ')
            if nxtVar < 0:
                print("Error! Variable can't negative!")
            else:
                break
        usDict[i] = nxtVar

    def myFunc(len, sum, k, s):
        if len == k:
            if sum == s:
                return 1
            else:
                return 0
        if len == 0:
            c = 1
        else:
            c = 0
        res = 0
        for i in range(c, 10):
            res += myFunc(len + 1, sum + i, k, s)
        return res
    return f"Result count: {myFunc(0, 0, usDict['k'], usDict['s'])}"


print(funcCreateVariabl())


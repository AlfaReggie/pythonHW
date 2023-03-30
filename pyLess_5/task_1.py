'''Напишите программу, которая на вход принимает два числа A и B,
 и возводит число А в целую степень B с помощью рекурсии.
*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''

def checkInput(message: str) -> float:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return float(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def addUserNums(progDict):
    for i in progDict.keys():
        progDict[i] = checkInput(f'Enter {i}: ')
    negative = False
    if progDict['B'] < 0:
        negative = True
        progDict['B'] *= -1
    def exponentF(progDict, expNum, negat) -> float:
        if progDict['B'] <= 0:
            if negat == False:
                return expNum
            return (1 / expNum)
        else:
            expNum *= progDict['A']
            progDict['B'] -= 1
            return exponentF(progDict, expNum, negat)

    return exponentF(progDict, 1, negative)

proDict = {'A': 2, 'B': 2}
print(addUserNums(proDict))

'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
*Пример:*

2 2
    4
'''

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        if int(checkNum) < 0:
            print("Error! Can't negative!")
            return checkInput(f'{message}')
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')


def addUserNums(list2num, count):
    def sumF(a, b, sumNum) -> int:
        if not a and not b:
            return sumNum
        elif a:
            return sumF(a - 1, b, sumNum + 1)
        elif b:
            return sumF(a, b - 1, sumNum + 1)
    if count == 0:
        return sumF(list2num[0], list2num[1], 0)
    list2num[count - 1] = checkInput(f'Enter: {count} number: ')
    return addUserNums(list2num, count - 1)

mlist = [0, 0]
print(addUserNums(mlist, len(mlist)))

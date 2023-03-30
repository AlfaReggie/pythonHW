'''
Дана последовательность натуральных чисел (одно число в строке),
завершающаяся числом 0. Определите значение второго по величине элемента
в этой последовательности, то есть элемента, который будет наибольшим,
если из последовательности удалить наибольший элемент.
В этой задаче нельзя использовать глобальные переменные. Функция получает данные,
считывая их с клавиатуры, а не получая их в виде параметра.
В программе на языке Python функция возвращает результат в виде кортежа
из нескольких чисел и функция вообще не получает никаких параметров.
В программе на языке C++ результат записывается в переменные,
которые передаются в функцию по ссылке. Других параметров,
кроме как используемых для возврата значения, функция не получает.
Гарантируется, что последовательность содержит хотя бы два числа (кроме нуля).
1 3 5 7 3 6 8 4 3 2 0 -> 7
1 2 3 4 5 6 3 1 2 5 3 -> 5
'''

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def createTuple():
    userList = []
    def myFunk() -> int:
        nxtNum = checkInput(f'Enter next number: ')
        print(nxtNum)
        if not nxtNum:
            if len(userList) <= 2:
                print("Error! Array can't less than 2 elements")
            else:
                return f'User tuple - {tuple(userList)}, the desired element - {userList[-2]}'
        else:
            if nxtNum not in userList:
                if not len(userList):
                    userList.append(nxtNum)
                elif len(userList) < 3:
                    if nxtNum < userList[-1]:
                        userList.insert(0, nxtNum)
                    else:
                        userList.append(nxtNum)
                else:
                    if nxtNum > userList[-1]:
                        userList.append(nxtNum)
                    elif nxtNum > userList[-2]:
                        userList.insert(-1, nxtNum)
                    else:
                        userList.insert(0, nxtNum)
        return myFunk()

    return myFunk()

print(createTuple())

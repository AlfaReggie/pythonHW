'''
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) `
**Вывод:**
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''

import numpy as np

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

def createMtrx():
    param = {'cols': 0, 'rows': 0}
    for p in param.keys():
        param[p] = checkInput(f'Enter {p} matrix: ')
    matriX = np.zeros((param['rows'], param['cols']))
    return matriX

def updateMtrx(f, i: int, j: int, matrix: np.array) -> float:
    if j == matrix.shape[1]:
        return matrix
    else:
        matrix[i, j] = f(i + 1, j + 1)
    while i != matrix.shape[0] - 1:
        return updateMtrx(f, i + 1, j, matrix)
    return updateMtrx(f, 0, j + 1, matrix)

def findElMtrx(matriX: np.array):
    paramFindName = ['findCol', 'findRow']
    paramFind = [0, 0]
    for fn in range(len(paramFind)):
        while True:
            coord = checkInput(f'Enter {paramFindName[fn]} matrix: ')
            if coord <= matriX.shape[fn]:
                paramFind[fn] = coord
                break
            else:
                print("Enter error!")
    return f"Matrix:\n {matriX} \n\n Your find element: {matriX[paramFind[0] - 1, paramFind[1] - 1]}"

def main():
    return findElMtrx(updateMtrx(lambda x, y: x * y, 0, 0, createMtrx()))

if __name__ == "__main__":
    print(main())



'''
def mtrxF(creatElF, findElF):
    matriX = []
    param = {'rows': 0, 'cols': 0}
    for p in param.keys():
        param[p] = checkInput(f'Enter {p} matrix: ')
    for i in range(1, param['rows'] + 1):
        nextRow = []
        for j in range(1, param['cols'] + 1):
            nextRow.append(creatElF(i, j))
        matriX.append(nextRow)
    matriX = np.array(matriX)
    def findEl(f):
        paramFind = {'findRow': 0, 'findCol': 0}
        for fn in paramFind.keys():
            nextCoord = checkInput(f'Enter {fn} matrix: ')
            paramFind[fn] = nextCoord
        return f"\nFind element: {f(paramFind['findRow'] - 1, paramFind['findCol'] - 1, matriX)}"
    return f"{matriX}\n {findEl(findElF)}"



print(mtrxF(lambda x, y: x * y, lambda x, y, matrix: matrix[x, y]))'''
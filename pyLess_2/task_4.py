''' *** (1)У вас есть массив чисел, составьте из них максимальное число. Например:

                                 [61, 228, 9] -> 961228'''

import numpy as np

while True:
    sizeArr = input('Enter count array elements: ')
    if sizeArr.isdigit() & sizeArr.isdigit() > 0:
        sizeArr = int(sizeArr)
        break
    else:
        print("Enter error! Try again!")

userList = []
for i in range(sizeArr):
    while True:
        nxtEl = input(f'Enter {i + 1} element: ')
        if nxtEl.isdigit():
            userList.append(int(nxtEl))
            break
        else:
            print("Enter error! Try again!")

userArr = np.array(userList)

print(''.join((sorted([str(x) for x in userArr], reverse=True))))

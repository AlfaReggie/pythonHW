'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

import math

while True:
    N = input('Enter count coints: ')
    if N.isdigit() & N.isdigit() > 0:
        N = int(N)
        break
    else:
        print("Enter error! Try again!")

for i in range(round(math.sqrt(N) + 1)):
    if 2 ** i < N:
        print(2 ** i)
    else:
        break
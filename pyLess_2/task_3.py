'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

'''import math

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
'''

'''*** (1)У вас есть массив чисел, составьте из них максимальное число. Например:

                                 [61, 228, 9] -> 961228'''

'''import numpy as np

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

'''

x = []
for i in range(10):
    x.append(str(i))
    if len(x) <= 1:
        pass
    else:
        head = ''

        tail = list(x)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in tail:
                x.append(head + s)
print(x)
print(tail)
print(head)


"""
def all_combinations(a):
    if len(a) <= 1:
        yield a
    else:
        head = ''

        tail = list(a)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in all_combinations(tail):
                yield [head] + s

a = list(all_combinations(tuple(map(str, range(1, 10)))))
print(a)"""
'''
def all_combinations(a):
    if len(a) <= 1:
        yield a
    else:
        head = ''
        
        tail = list(a)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in all_combinations(tail):
                yield [head] + s

def all_signs(n):
    if n == 0:
        yield ()
    else:
        for tail in all_signs(n-1):
            for s in '+-':
                yield (s,) + tail

def perform_operations(nums, signs):
    nums = list(map(int, nums))
    result = nums.pop(0)
    n = 1
    for s in signs:
        if s == '+':
            result += nums.pop(0)
        if s == '-':
            result -= nums.pop(0)
        n += 1
    return result

for numbers in all_combinations(tuple(map(str, range(1, 10)))):
    #print(numbers)
    for signs in all_signs(len(numbers) - 1):
        #print(signs)
        summ = perform_operations(numbers, signs)
        if summ == 100:
            print(
                ''.join(map(
                    lambda x: ''.join(x),
                    zip(numbers, signs)))
                + numbers[-1])'''

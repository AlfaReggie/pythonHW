'''str_1 = 'a a a b c a a d c d a b';

def twinCntr(str_1):
    str_1 = str_1.split(' ')
    temp = []

    for i in range(len(str_1)):
        counter = 0
        for j in str_1[:i]:
            if str_1[i] == j:
                counter += 1
        if counter > 0:
            counter = f'_{counter}'
        else:
            counter = ' '

        temp.append(f'{str_1[i]}{counter}')

    print(temp)

twinCntr(str_1)'''

aN = [1, 2, 3]
aM = [2, 5, 1]

def rec_is(aN, aM, i):
    if i == len(aM) - 1:
        return aN
    else:
        if aN[i] in aM:
            aN.remove(aN[i])
            return rec_is(aN, aM, i)
        else:
            return rec_is(aN, aM, i + 1)

print(rec_is(aN, aM, 0))
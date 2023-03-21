str_1 = 'a a a b c a a d c d a b';

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

twinCntr(str_1)
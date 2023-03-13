'''Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками
  (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no'''

questList = ['row', 'col', 'count pieces']
userList = []

for i in range(3):
    while True:
        userInput = input(f'Enter {questList[i]}: ')
        if userInput.isdigit():
            userList.append(int(userInput))
            break
        else:
            print("Enter error. Try again!")

if (userList[2] % userList[1] == 0)\
    | (userList[2] % userList[0] == 0)\
    & (userList[0] * userList[1] > userList[2]):
    print('Yes')
else:
    print('No')
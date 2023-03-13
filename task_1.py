"""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
*** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного"""

sym_rep = [';', ',', '.']
while True:
    userNum = input("Enter 3 digits number: ")
    if userNum.isdigit():
        if len(userNum) == 3:
            num_r = int(userNum)
            break
        else:
            print("Enter error, need 3 digits!")
    else:
        for i in sym_rep:
            if i in userNum:
                userNum = userNum.replace(i, '')
                break
        if userNum.isdigit():
            num_r = int(userNum)
            break
        else:
            print("Enter error, need number!")

sum = 0
while num_r > 0:
    sum += num_r % 10
    num_r //= 10

print(sum)


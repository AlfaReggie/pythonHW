'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no
******** Рассмотрите вариант разделения на правую и левую часть произвольно,
но не меняя порядок цифр.'''

while True:
    tickNum = input("Enter cranes count: ")
    if tickNum.isdigit():
        if len(tickNum) == 6:
            break
        else:
            print("It's not happy ticket!")
    else:
        print("It's not number, try again!")

sum_parts = [0, 0]
tickNumDig = int(tickNum)

for i in range(len(sum_parts)):
    for j in range(len(tickNum)//2):
        sum_parts[i] += tickNumDig % 10
        tickNumDig //= 10

if sum_parts[1] == sum_parts[0]:
    print('yes')
else:
    print('no')
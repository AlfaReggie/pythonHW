''' Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

helpNums = {'sum' : 0, 'mult' : 0}
for i in range(len(helpNums)):
    while True: # запускае бесконечный цикл
        usrNum = input(f'Enter {list(helpNums.keys())[i]} numbers: ') # просим пользователя ввести очередное число
        if usrNum.isdigit(): # проверяем что значение является числом
            helpNums[list(helpNums.keys())[i]] = int(usrNum) # переводим значение в целочисленный тип и добавляем в список
            break # останавливаем цикл
        else:
            print("Enter error! Try again!")

print(helpNums.items())

for i in range(list(helpNums.values())[0]):
    for j in range(list(helpNums.values())[1]):
        if (i + j == list(helpNums.values())[0]) & (i * j == list(helpNums.values())[1]):
            print(i, j)
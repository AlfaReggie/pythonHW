'''Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
******Рассмотрите вариант, что он также делают журавлики в момент подсчета
 и известно только число уже полностью готовых'''

while True:
    cranCount = input("Enter cranes count: ")
    if cranCount.isdigit():
        cntCran = int(cranCount)
        if cntCran & 1:
            cntCran -= 1
        break
    else:
        print('Enter error! Try again: ')
print('Number of layers finished: ', cntCran)

for i in range(1, cntCran//6+1):
    if i * 6 == cntCran:
        print(f'{i} {4*i} {i}')




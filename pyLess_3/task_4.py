'''
*****(3)Напишите программу, которая принимает на вход две строки и определяет,
 являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.

Пример ввода:
Цари, вино и сало.
Лисица и ворона.

Пример вывода:
YES
'''

def checkInput(message):
    while True:
        userTxt = input(message)
        for i in [' ', ',', '.']:
            userTxt = userTxt.replace(i, '')
        print(userTxt)
        if userTxt.isalpha():
            return sorted(userTxt.upper())
        else:
            print("Enter error!")


def checkAnagram():
    while True:
        countChecks = input("Enter counts texts for test: ")
        if countChecks.isdigit():
            break
        else:
            print('Enter error, need number: ')

    textsList = []
    for i in range(int(countChecks)):
        textsList.append(checkInput(f'Enter {i + 1} text: '))
        if len(textsList) > 1:
            if (len(textsList[i]) != len(textsList[i - 1])) or textsList[i] != textsList[i - 1]:
                return "NO"
                break
    return "YES"

print(checkAnagram())

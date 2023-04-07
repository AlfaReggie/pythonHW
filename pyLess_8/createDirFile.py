'''
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать
функционал для изменения и удаления данных
'''

import os

def checkInput(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        if int(checkNum) < 0:
            print("Error! Can't negative!")
            return checkInput(f'{message}')
        return int(checkNum)
    else:
        print("Error!")
        return checkInput(f'{message}')

def ensure_dir(dirname):
    return os.makedirs(dirname, exist_ok=True)

def createFile(nameFile, dirName):
    return open(os.path.join(os.path.dirname(__file__), dirName, f'{nameFile}.txt'), 'w')

'''def writeInF(nameFile):
    with open(nameFile, 'a+', encoding='UTF-8') as m_file:
        m_file.write(f'{input("Enter: ")}\n')
    return m_file'''

def showDir(dirname) -> None:
    print('Files: ')
    for i, val in enumerate(os.listdir(dirname)):
        print(f"{i + 1} - {val}")

'''def openDir():
    return os.listdir('LibDir')'''

def openFile(nameFile):
    with open(nameFile, 'r', encoding='UTF-8') as m_file:
        for i in m_file:
            print(i)

def choiseCommand(flag):
    comandMain = ["Open libraris", "Stop program"]
    comandLibr = ['Create new file', "Choise file", "Exit to main"]
    comandFile = ["Update file", 'Delete file', "Exit to main"]
    lstCmd = [comandMain, comandLibr, comandFile]
    print('\nCommands: ')
    for i, val in enumerate(lstCmd[flag]):
        print(f"{i + 1}: {val}")

def menu(exit):
    if exit == True:
        main(False)
    ensure_dir('LibDir')
    choiseCommand(0)
    userAnswMain = checkInput('\nChoise command:')
    if userAnswMain == 1:
        showDir('LibDir'), choiseCommand(1)
        userAnswLibr = checkInput('\nChoise command:')
        if userAnswLibr == 1:
            createFile(input('Enter file name: '), 'LibDir')
            showDir('LibDir'), choiseCommand(1)
            choiseCommand(2)
            userAnswFails = checkInput('\nChoise command:')
            openFile(f'LibDir/{os.listdir("LibDir")[checkInput("Choise file: ") - 1]}')
        else:
            menu(False)

    else: main(False)


def main(q):
    if q == False:
        print('Ok, Bye!')
        return
    print(f'Start program...')
    menu(False)

if __name__ == '__main__':
    main(True)

'''def main(flag):
    if flag == False:
        return
    while True:
        ensure_dir('directory')
        choiseCommand(0)
        userAnswMain = checkInput('\nChoise command:')
        if userAnswMain == 1:
            print('\nYour files')
            showDir('directory')
            print('\n')
            choiseCommand(userAnswMain)
            userAnsw = checkInput('\nChoise command: ')
            if userAnsw == 1:
                showDir('directory')
                userChoise = checkInput("Enter number file: ")
                pathFile = f"directory/{openDir()[userChoise - 1]}"
                openFile(pathFile)
                choiseCommand(2)
                userAnswFile = checkInput('\nChoise command: ')
                if userAnswFile == 1:
                    writeInF(pathFile)'''

'''print(f'Use dir - {os.getcwd()}')
#os.mkdir('directory')
os.chdir('directory')
print(f'Use dir>>> - {os.getcwd()}')
os.chdir('..')
print(f'Use dir<<< - {os.getcwd()}')'''
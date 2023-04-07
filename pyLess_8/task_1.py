'''
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать
функционал для изменения и удаления данных
'''

import os

def checkInputStr(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isalpha():
        return checkNum
    else:
        print("Error!")
        return checkInputStr(f'{message}')

def checkInputInt(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        if int(checkNum) < 0:
            print("Error! Can't negative!")
            return checkInputInt(f'{message}')
        return int(checkNum)
    else:
        print("Error!")
        return checkInputInt(f'{message}')

def ensureDir(dirname):
    return os.makedirs(dirname, exist_ok=True)

def createFile(nameFile, dirName):
    return open(os.path.join(os.path.dirname(__file__), dirName, f'{nameFile}.txt'), 'w')

def showDir(dirname) -> None:
    print('Files: ')
    if len(os.listdir(dirname)) < 1:
        print('Not files')
        choiseCommand(2)
    else:
        for i, val in enumerate(os.listdir(dirname)):
            print(f"{i + 1} - {val}")
        choiseCommand(1)

def deleteFile(fileName):
    return os.remove(fileName)

def writeInF(nameFile):
    with open(nameFile, 'a+', encoding='UTF-8') as m_file:
        contName = checkInputStr('Enter name: ')
        contFamName = checkInputStr('Enter family name: ')
        contNumber = checkInputInt('Enter phone number: ')
        m_file.write(f"{contName} {contFamName} {contNumber}\n")
    return m_file

def openDir():
    return os.listdir('LibDir')

def openFile(nameFile):
    with open(nameFile, 'r', encoding='UTF-8') as m_file:
        for i in m_file:
            print(i)

def choiseCommand(flag):
    comandMain = ["Open libraris", "Stop program"]
    comandLibrZero = ['Create new file', "Exit to main"]
    comandLibr = ['Create new file', "Choise file", "Exit to main"]
    comandFile = ["Update file", 'Delete file', "Exit to main"]
    comandContact = ["Add contact", "Update contacts", 'Delete contacts', 'Exit to files']
    lstCmd = [comandMain, comandLibr, comandLibrZero, comandFile, comandContact]
    print('\nCommands: ')
    for i, val in enumerate(lstCmd[flag]):
        print(f"{i + 1}: {val}")

def menuMain(exit):
    if exit == True:
        return main(True)
    ensureDir('LibDir')
    choiseCommand(0)
    userAnswMain = checkInputInt('\nChoise command:')
    if userAnswMain == 1:
        showDir('LibDir')
    else:
        return main(True)
    def menuLib(exit):
        if exit == True:
            menuLib(False)
        userAnswLibr = checkInputInt('\nChoise command:')
        if userAnswLibr == 1:
            createFile(input('Enter file name: '), 'LibDir')
            showDir('LibDir')
            menuLib(False)
        elif userAnswLibr == 2:
            fileName = f"LibDir/{openDir()[checkInputInt('Enter number file: ') - 1]}"
            openFile(fileName)
            def menuFail(exit):
                if exit == True:
                    menuFail(False)
                choiseCommand(3)
                userAnswFile = checkInputInt('\nChoise command: ')
                if userAnswFile == 1:
                    def menuContact(exit):
                        if exit == True:
                            menuFail(False)
                        choiseCommand(4)
                        userAnswCont = checkInputInt('\nChoise command:')
                        if userAnswCont == 1:
                            writeInF(fileName)
                            openFile(fileName)
                            menuContact(False)
                        elif userAnswCont == 2:
                            pass
                        elif userAnswCont == 3:
                            pass
                        else:
                            menuFail(False)
                elif userAnswFile == 2:
                    deleteFile(fileName)
                    menuLib(False)
                else:
                    menuLib(False)
                menuContact(False)
            menuFail(False)
        menuMain(False)
    menuLib(False)

def main(exit):
    if exit == True:
        print('Bye!')
        return
    print(f'Start program...')
    menuMain(False)

if __name__ == '__main__':
    main(False)

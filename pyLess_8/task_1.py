'''
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать
функционал для изменения и удаления данных
'''

import os, re

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

def deleteFile(fileName):
    return os.remove(fileName)

def writeInF(nameFile):
    with open(nameFile, 'a+', encoding='UTF-8') as m_file:
        contName = checkInputStr('Enter name: ')
        contFamName = checkInputStr('Enter family name: ')
        contNumber = checkInputInt('Enter phone number: ')
        m_file.write(f"{contName} {contFamName} {contNumber}\n")
    return m_file

def delCont(file, numCont, flag):
    with open(file) as f:
        lines = f.readlines()
    delStr = lines[numCont]
    pattern = re.compile(re.escape(delStr))
    with open(file, 'w') as f:
        if flag == 'del':
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    f.write(line)
        elif flag == 'upd':
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    f.write(line)
                else:
                    contName = checkInputStr('Enter name: ')
                    contFamName = checkInputStr('Enter family name: ')
                    contNumber = checkInputInt('Enter phone number: ')
                    f.write((f"{contName} {contFamName} {contNumber}\n"))

def openDir():
    return os.listdir('LibDir')

def openFile(nameFile):
    if sum(1 for line in open(nameFile)) > 0:
        with open(nameFile, 'r', encoding='UTF-8') as m_file:
            for i, val in enumerate(m_file):
                print(f"{i + 1}: {val}")
    else:
        print('Fail...')

def choiseCommand(flag):
    comandMain = ["Open libraris", "Stop program"]
    comandLibrZero = ['Create new file', "Exit to main"]
    comandLibr = ['Create new file', "Choise file", "Exit to main"]
    comandFile = ["Update file", 'Delete file', "Exit to library"]
    comandContZero = ["Add contact", 'Exit to files']
    comandContact = ["Add contact", "Update contacts", 'Delete contacts', 'Exit to files']
    lstCmd = [comandMain, comandLibr, comandLibrZero, comandFile, comandContZero, comandContact]
    print('\nCommands: ')
    for i, val in enumerate(lstCmd[flag]):
        print(f"{i + 1}: {val}")
    return len(lstCmd[flag])

def checkComm(flag):
    userAnsw = checkInputInt('\nSelect command:')
    if userAnsw > flag:
        print('Not find command!')
        return checkComm(flag)
    else:
        return int(userAnsw)

def menuMain():
    ensureDir('LibDir')
    answ = checkComm(choiseCommand(0))
    if answ == 1:
        menuLib(False, 'LibDir')
    else:
        print('Bye!')

def menuLib(exit, dirname):
    if exit == True:
        menuMain()
    print('Files: ')
    if len(os.listdir(dirname)) < 1:
        print('Not files')
        answ = checkComm(choiseCommand(2))
        if answ == 1:
            createFile(input('Enter file name: '), 'LibDir')
            menuLib(False, 'LibDir')
        else:
            menuMain()
    else:
        for i, val in enumerate(os.listdir(dirname)):
            print(f"{i + 1} - {val}")
        answ = checkComm(choiseCommand(1))
        if answ == 1:
            createFile(input('Enter file name: '), 'LibDir')
            menuLib(False, 'LibDir')
        elif answ == 2:
            while True:
                fileNum = checkInputInt('Enter number file: ')
                if fileNum <= len(os.listdir(dirname)): break
                else: print('Not find file!')
            fileName = f"LibDir/{openDir()[fileNum - 1]}"
            openFile(fileName)
            menuFail(False, fileName)
        else:
            menuMain()

def menuFail(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    answ = checkComm(choiseCommand(3))
    if answ == 1:
        menuContact(False, fileName)
    elif answ == 2:
        deleteFile(fileName)
        menuLib(False, 'LibDir')
    else:
        menuMain()

def menuContact(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    if sum(1 for line in open(fileName)) != 0:
        answ = checkComm(choiseCommand(5))
        if answ == 1:
            writeInF(fileName)
            openFile(fileName)
            menuContact(False, fileName)
        elif answ == 2:
            openFile(fileName)
            while True:
                numStr = checkInputInt("Select contact: ")
                if numStr <= sum(1 for line in open(fileName)): break
                else: print('Not find contact!')
            delCont(fileName, numStr - 1, 'upd')
            menuContact(False, fileName)
        elif answ == 3:
            openFile(fileName)
            while True:
                numStr = checkInputInt("Select contact: ")
                if numStr <= sum(1 for line in open(fileName)): break
                else: print('Not find contact!')
            delCont(fileName, numStr - 1, 'del')
            openFile(fileName)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)
    else:
        choiseCommand(5)
        userAnswCont = checkInputInt('\nSelect command:')
        if userAnswCont == 1:
            writeInF(fileName)
            openFile(fileName)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)

def main():
    print(f'Start program...')
    menuMain()

if __name__ == '__main__':
    main()
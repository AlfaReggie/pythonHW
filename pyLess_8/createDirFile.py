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

def writeInF(nameFile):
    with open(nameFile, 'a+', encoding='UTF-8') as m_file:
        m_file.write(f'{input("Enter: ")}\n')
    return m_file

def showDir(dirname) -> None:
    for i, val in enumerate(os.listdir(dirname)):
        print(f"{i + 1}: {val}")

def openDir():
    return os.listdir('directory')

def openFile(nameFile):
    with open(nameFile, 'r', encoding='UTF-8') as m_file:
        for i in m_file:
            print(i)

def choiseCommand(flag):
    comandMain = ["Open libraris", "Stop program"]
    comandLibr = ["Choise file", "Exit to main"]
    comandFile = ["Update file", 'Create new file', 'Delete file', "Exit to main"]
    lstCmd = [comandMain, comandLibr, comandFile]
    for i, val in enumerate(lstCmd[flag]):
        print(f"{i + 1}: {val}")

def menu(flag):
    pass

def main() -> None:
    print('Start program')
    print(filePath('directory', '1.txt'))

'''answ_user = input("Enter y if you want create file and write anything in file: ")
if answ_user.lower() == 'y':
    filename = input('Enter name file: ')
    userFile = createFile(filename)
    while True:
        user_enter = input('Enter surname and prem: ')
        if not user_enter:
            break
        else:
            writeInF(file_user, user_enter)'''

'''createDir('testDir')
createFile('test', 'testDir')'''
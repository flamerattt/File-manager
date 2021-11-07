import os
import sys
import shutil
import settings as stngs

path = "/Users/anna/File_Manager"
stngs.start()

def help_list():
    print('''Отображение всех команд [команда] - help
    Узнать текущее местонахождение пользователя [команда] - wiam
    Посмотреть содержимое папки [команда] – lsdr
    Создание папки [команда, имя] - mkdr
    Удаление папки по имени [команда, имя] - dldr
    Создание пустого текстового файла [команда, имя] - mkfl
    Записать текст в файл [команда, имя] - wrtfl
    Показать содержимое файла [команда, имя] - shw
    Удаление файла по имени [команда, имя] - dlfl
    Скопировать файл [команда, имя_файла, путь] - cpfl
    Переместить файл [команда, имя_файла, путь] - mvfl
    Переимновать файл [команда, имя1, имя2] - rnmfl
    Спуститься в директории на один уровень ниже [команда, имя] - tpdwn
    Подняться в директории на один уровень выше [команда] - tpup
    Выход из программы [команда] - exit''')


def wiam():
    print(os.getcwd())


def mkdr(dirName):
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print('file already exists')


def dldr(dirName):
    try:
        os.rmdir(dirName)
    except FileNotFoundError:
        print('directory does not exist')


def mkfl(fileName):
    file = open(fileName, "w+")
    file.close()


def wrtfl(filename, w):
    try:
        f = open(filename, "a")
        f.write(w)
        f.close()
    except FileExistsError:
        print('file does not exist')


def shw(fileName):
    try:
        file = open(fileName, "r")
        print(file.read())
        file.close()
    except FileExistsError:
        print('file does not exists')


def dlfl(fileName):
    try:
        os.remove(fileName)
    except FileExistsError:
        print('file does not exist')


def cpfl(fileName, newFilename):
    try:
        shutil.copy(fileName, newFilename)
    except FileExistsError:
        print('file does not exist')


def mvfl(fileName, newFilename):
    try:
        shutil.move(fileName, newFilename)
    except FileExistsError:
        print('file does not exist')


def rnmfl(fileName, newFilename):
    try:
        os.rename(fileName, newFilename)
    except FileExistsError:
        print('file does not exist')


def tpdwn(dirName):
    try:
        OS = sys.platform
        if OS == 'darwin':
            a = os.getcwd()
            os.chdir(a + '/' + dirName)
            print(os.getcwd())

        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            os.chdir(a + '\\' + dirName)
            print(os.getcwd())
    except FileNotFoundError:
        print('directory do not exist')

def lsdr(dirName):
    try:
        list_in_dir = os.listdir(dirName)
        print(list_in_dir)
    except FileNotFoundError:
        print('directory do not exist')


def tpup():
    try:
        z = os.getcwd()
        if len(os.path.split(os.getcwd())[0]) < len(path):
            print('Выход за пределы рабочей папки')
        elif len(os.path.split(os.getcwd())[0]) <= len(z) or len(os.path.split(os.getcwd())[0]) + 1 <= len(z):
            OS = sys.platform
            # print(OS)
            if OS == 'darwin':
                a = os.getcwd()
                b = a.split('/')
                del b[-1]
                a = '/'.join([str(item) for item in b])
                os.chdir(a)
                print(os.getcwd())

            elif OS == 'cygwin' or OS == 'win32':
                a = os.getcwd()
                b = a.split('\\')
                del b[-1]
                a = '\\'.join([str(item) for item in b])
                os.chdir(a)
                print(os.getcwd())
        else:
            print("cant go further")
            print(os.getcwd())
    except:
        print('cant go up')



while True:
    try:
        command = input('Введите команду (help - список всех команд): ')
        command = command.split(' ')
        if command[0] == 'exit':
            sys.exit()
        elif command[0] == 'help':
            help_list()
        elif command[0] == 'mkdr':
            mkdr(command[1])
        elif command[0] == 'dldr':
            dldr(command[1])
        elif command[0] == 'mkfl':
            mkfl(command[1])
        elif command[0] == 'shw':
            shw(command[1])
        elif command[0] == 'wrtfl':
            contentWrap = input("Текст: ")
            wrtfl(command[1], contentWrap)
        elif command[0] == 'wiam':
            wiam()
        elif command[0] == 'dlfl':
            dlfl(command[1])
        elif command[0] == 'cpfl':
            cpfl(command[1], command[2])
        elif command[0] == 'mvfl':
            mvfl(command[1], command[2])
        elif command[0] == 'rnmfl':
            rnmfl(command[1], command[2])
        elif command[0] == 'tpdwn':
            tpdwn(command[1])
        elif command[0] == 'tpup':
            tpup()
        elif command[0] == 'lsdr':
            lsdr(command[1])
        else:
            print('Команды не существует')
    except:
        print('Команда введена неправильно')
import sys
import os


def makeLine(t, argv, mode):
    if mode == 0:
        if argv in t:
            t = t.replace(argv, '\033[30;43m' + argv + '\033[0m')
    if mode == 1:
        check = []
        word = ''
        if argv.lower() in t.lower():
            for i in range(len(t)):
                word = t[i:i + len(argv)]
                if word.lower() == argv.lower():
                    if word not in check:
                        check.append(word)
                        t = t.replace(word, '\033[30;43m' + word + '\033[0m')
    return t


def main(item):
    if '--case-sensitive' not in sys.argv and '--hidden' not in sys.argv:
        if not os.path.isfile(sys.argv[-1]):
            openFile(sys.argv[-2], 1, 0)
        else:
            changeFile(sys.argv[-1], sys.argv[-2], 0)
    elif sys.argv[-2] == '--case-sensitive' or sys.argv[-2] == '--hidden':
        if '--case-sensitive' in sys.argv and '--hidden' in sys.argv:
            openFile(sys.argv[-1], 0, 1)
        elif '--case-sensitive' in sys.argv:
            openFile(sys.argv[-1], 0, 0)
        else:
            openFile(sys.argv[-1], 1, 1)
    elif sys.argv[-3] == '--case-sensitive' or sys.argv[-3] == '--hidden':
        if not os.path.isfile(sys.argv[-1]):
            if '--case-sensitive' in sys.argv and '--hidden' in sys.argv:
                openFile(sys.argv[-2], 0, 1)
            elif '--case-sensitive' in sys.argv:
                openFile(sys.argv[-2], 0, 0)
            else:
                openFile(sys.argv[-2], 1, 1)
        else:
            if '--case-sensitive' in sys.argv and '--hidden' in sys.argv:
                changeFile(sys.argv[-1], sys.argv[-2], 0)
            elif '--case-sensitive' in sys.argv:
                changeFile(sys.argv[-1], sys.argv[-2], 0)
            else:
                changeFile(sys.argv[-1], sys.argv[-2], 1)


def openFile(item, mode, hidden):
    files = os.listdir()
    if hidden == 1:
        for file in files:
            print('\033[1;32m'+file + '\033[0m')
            changeFile(file,item,mode)
    if hidden == 0:
        for file in files:
            if file[0] != '.':
                print('\033[1;32m'+file + '\033[0m')
                changeFile(file,item,mode)


def changeFile(file,item,mode):
        file = open(file, "r")
        content = file.read()
        content = content.split('\n')
        for i in range(len(content)-1):
            if mode == 1:
                if item.lower() in content[i].lower():
                    print('\033[1;33m' + str(i+1)+'\033[0m', end=":")
                    print(makeLine(content[i], item, mode))
            if mode == 0:
                if item in content[i]:
                    print('\033[1;33m' + str(i+1)+'\033[0m', end=":")
                    print(makeLine(content[i], item, mode))
main(sys.argv)

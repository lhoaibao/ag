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


def caseSensitive(item):
    if sys.argv[1] == '--case-sensitive':
        if os.path.isfile(sys.argv[3]):
            changeFile(sys.argv[3], sys.argv[2], 0)
    else:
        if os.path.isfile(sys.argv[2]):
            changeFile(sys.argv[2], sys.argv[1], 1)


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


caseSensitive(sys.argv)

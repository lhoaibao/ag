import sys
import os


def makeLine(nd, argv, mode):
    if mode == 0:
        if argv in nd:
            nd = nd.replace(argv, '\033[30;43m' + argv + '\033[0m')
    if mode == 1:
        if argv.lower() in nd.lower():
            for i in range(len(nd)):
                a = i
                j = 0
                w = ''
                while argv[j].lower() == nd[a].lower():
                    if j != len(argv) - 1:
                        w += nd[a]
                        a += 1
                        j += 1
                    else:
                        if argv[j].lower() == nd[a].lower():
                            w += nd[a]
                            nd = nd.replace(w, '\033[30;43m' + w + '\033[0m')
                            break
                        else:
                            break
    return nd


def caseSensitive(item):
    if sys.argv[1] == '--case-sensitive':
        if len(sys.argv) < 4:
            files = os.listdir()
            for file in files:
                if os.path.isfile(file):
                    print('\033[1;32m' + file + '\033[0m')
                    file = open(file, "r")
                    content = file.read()
                    content = content.split('\n')
                    for i in range(len(content)-1):
                        if sys.argv[2] in content[i]:
                            print('\033[1;33m' + str(i+1)+'\033[0m', end=":")
                            print(makeLine(content[i], sys.argv[2], 0))
                    file.close()
        elif os.path.isfile(sys.argv[3]):
            file = open(sys.argv[3], "r")
            content = file.read()
            content = content.split('\n')
            for i in range(len(content)-1):
                if sys.argv[2] in content[i]:
                    print('\033[1;33m' + str(i+1)+'\033[0m', end=":")
                    print(makeLine(content[i], sys.argv[2], 0))
    else:
        if len(sys.argv) < 3:
            files = os.listdir()
            for file in files:
                if os.path.isfile(file):
                    print('\033[1;32m'+file + '\033[0m')
                    file = open(file, "r")
                    content = file.read()
                    content = content.split('\n')
                    for i in range(len(content)-1):
                        if sys.argv[1].lower() in content[i].lower():
                            print('\033[1;33m' + str(i+1)+'\033[0m', end=":")
                            print(makeLine(content[i], sys.argv[1], 1))
        elif os.path.isfile(sys.argv[2]):
            file = open(sys.argv[2], "r")
            content = file.read()
            content = content.split('\n')
            for i in range(len(content)-1):
                if sys.argv[1].lower() in content[i].lower():
                    print('\033[1;33m' + str(i+1)+'\033[0m', end=":")
                    print(makeLine(content[i], sys.argv[1], 1))


caseSensitive(sys.argv)

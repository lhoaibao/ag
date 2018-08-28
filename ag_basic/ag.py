import sys
import os


def caseSensitive(item):
    if sys.argv[1] == '--case-sensitive':
        if os.path.isfile(sys.argv[3]):
            file = open(sys.argv[3],"r")
            content = file.read()
            content = content.split('\n')
            for i in range(len(content)-1):
                if sys.argv[2] in content[i]:
                    print('\033[1;33m'+str(i + 1)+'\033[0m'+':',content[i])
    else:
        if os.path.isfile(sys.argv[2]):
            file = open(sys.argv[2],"r")
            content = file.read()
            content = content.split('\n')
            for i in range(len(content)-1):
                if sys.argv[1] in content[i].lower():
                    print('\033[1;33m'+str(i + 1)+'\033[0m'+':',content[i])

caseSensitive(sys.argv)

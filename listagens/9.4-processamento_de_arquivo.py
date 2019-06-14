LINE_WIDTH = 40

import sys
try:
    fileName = sys.argv[1]
except IndexError:
    fileName = 'entrada.txt'
entrada = open(fileName)
for line in entrada.readlines():
    inicio, resto = line[0], line[1:]
    if inicio == ';':
        continue
    elif inicio == '>':
        print(resto.rjust(LINE_WIDTH))
    elif inicio == '*':
        print(resto.center(LINE_WIDTH))
    else:
        print(resto)


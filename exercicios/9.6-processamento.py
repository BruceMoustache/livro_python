lineWidth = 74
entrada = open('entrada.txt')
for line in entrada.readlines():
    begin, rest = line[0], line[1:]
    if begin == ';':
        continue
    elif begin == '*':
        print(rest.center(lineWidth))
    elif begin == '>':
        print(rest.rjust(lineWidth))
    elif begin == '=':
        #print(rest * lineWidth)
        print(begin * 40)
    elif begin == '.':
        input()
    else:
        print(rest)


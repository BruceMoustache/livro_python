LINES_COUNT = 60

def readPaging(fileName):
    global LINES_COUNT
    opened = open(fileName)
    text = opened.read()
    pages = dividePages(text, LINES_COUNT)
    for page in pages:
        print(page)
        input()

def dividePages(text, linesCount):
    pages = []
    lines = text.splitlines()
    
    begin = 0
    end = linesCount
    while end != len(lines):
        pages.append(text[begin:end])

        begin += linesCount
        end += linesCount

    return pages

readPaging('ler.txt')


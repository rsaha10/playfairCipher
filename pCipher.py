import sys

encodeDecode = sys.argv[1]
txt = sys.argv[2].replace("J", "I")
key = sys.argv[3]

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

for x in key:
    if x in alphabet:
        alphabet = alphabet.replace(x, "")

key = key + alphabet

matrix = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

ind = 0
for x in range(5):
    for y in range(5):
        matrix[x][y] = key[ind]
        ind+=1

def makePair(text):
    for x in range(0, len(text), 2):
        if text[x] == text[x+1]:
            text = text[0:x+1] + "X" + text[x+1:len(text)]

    if len(text)%2 == 1:
        text = text + "X"

    pairs = []

    for x in range(0, len(text), 2):
        pairs.append(text[x:x+2])

    return pairs

pairs = makePair(txt)

def horizontalEncode(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==x:
             xRow = i
             xCol = k

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==y:
             yRow = i
             yCol = k

    str = matrix[(xRow+1)%5][xCol] + matrix[(yRow+1)%5][yCol]
    return str

def verticalEncode(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==x:
                xRow = i
                xCol = k

    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==y:
                yRow = i
                yCol = k

    str = matrix[xRow][(xCol+1)%5] + matrix[yRow][(yCol+1)%5]
    return str

def regEncode(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==x:
                xRow = i
                xCol = k

    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==y:
                yRow = i
                yCol = k

    str = matrix[xRow][yCol] + matrix[yRow][xCol]
    return str

def choose(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==x:
             xRow = i
             xCol = k

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==y:
             yRow = i
             yCol = k

    if xRow == yRow:
        return horizontalEncode(str)
    if xCol == yCol:
        return verticalEncode(str)
    else:
        return regEncode(str)

finalMessage = ""

if encodeDecode == "encode":
    for i in pairs:
        finalMessage = finalMessage + choose(i)

    print (finalMessage)

def horizontalDecode(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==x:
             xRow = i
             xCol = k

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==y:
             yRow = i
             yCol = k

    xRow = xRow - 1
    if xRow == -1:
        xRow == 4
    yRow = yRow - 1
    if yRow == -1:
        yRow == 4

    str = matrix[xRow][xCol] + matrix[yRow][yCol]
    return str

def verticalDecode(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==x:
                xRow = i
                xCol = k

    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==y:
                yRow = i
                yCol = k

    xCol = xCol - 1
    if xCol == -1:
        xCol == 4
    yCol = yCol - 1
    if yCol == -1:
        yCol == 4

    str = matrix[xRow][xCol] + matrix[yRow][yCol]
    return str

def chooseD(str):
    x = str[0]
    y = str[1]

    xRow = 0
    xCol = 0
    yRow = 0
    yCol = 0

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==x:
             xRow = i
             xCol = k

    for i,j in enumerate(matrix):
       for k,l in enumerate(j):
         if l==y:
             yRow = i
             yCol = k

    if xRow == yRow:
        return horizontalDecode(str)
    if xCol == yCol:
        return verticalDecode(str)
    else:
        return regEncode(str)

if encodeDecode == "decode":
    for i in pairs:
        finalMessage = finalMessage + chooseD(i)

    print (finalMessage)

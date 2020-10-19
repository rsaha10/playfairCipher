# Lots of bugs that I weren't able to fix :(
#1) my function for inserting Xs does not work for any case I tries
#mississippi >> out of bounds error
#mississipp >> returns "MISXSISXSI" (what happened to the last 2 ps)
#2) None of my functions for actually returning the encoded letter pairs work :(

userInput = input("Please input whether you would like to encode or decode, followed by ciphertext or plaintext, and lastly your desired keytext: ").upper()

x = userInput.split()
ED = x[0]
text = x[1]
key = None

if len(x) < 3:
    key = None
else:
    key = x[2]

L = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]


alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

if key != None:
    for x in key:
        if (x in alphabet) == True:
            alphabet = alphabet.replace(x, "")

    keyAlph = list(key + alphabet)

    L[0] = keyAlph[0:4]
    L[1] = keyAlph[4:9]
    L[2] = keyAlph[9:14]
    L[3] = keyAlph[14:19]
    L[4] = keyAlph[19:24]
pairList = []

#---------------------------------------#
def insertX(str):
    for x in range(0, len(str), 2):
        if str[x]==str[x+1]:
            str = str[0:x+1] + "x" + str[x+1:-1]

    return str

        # how do i do this :(
#---------------------------------------#
def verticalEncode(letter1, letter2):
    let1x = 0
    let2x = 0
    letY = 0

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter1:
            let1x = (x + 1) % 5
            letY = z

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter1:
            let2x = (x + 1) % 5

    return (L[let1x][letY] + L[let2x][letY])
#---------------------------------------#
def horizontalEncode(letter1, letter2):
    let1y = 0
    let2y = 0
    letX = 0

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter1:
            let1y = (z + 1) % 5
            letX = x

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter1:
            let2y = (z + 1) % 5

    return (L[letX][let1y] + L[letX][let2y])
#---------------------------------------#
def regularEncode(letter1, letter2):
    let1x = 0
    let1y = 0
    let2x = 0
    let2y = 0

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter1:
            let1x = x
            let1y = z

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter2:
            let2x = x
            let2y = z
    return (L[let1x][let2y] + L[let2x][let1y])
#---------------------------------------#
encodedMessage = ""

def choose(letter1, letter2):
    let1x = 0
    let1y = 0
    let2x = 0
    let2y = 0

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter1:
            let1x = x
            let1y = z

    for x,y in enumerate(L):
       for z,a in enumerate(y):
         if a==letter2:
            let2x = x
            let2y = z

    if let1x == let2x:
        encodedMessage = encodedMessage + horizontalEncode(letter1, letter2)

    if let1y == let2y:
        encodedMessage = encodedMessage + verticalEncode(letter1, letter2)

    if let1x != let2x and let1y != let2y:
        encodedMessage = encodedMessage + regularEncode(letter1, letter2)

print (insertX(text))

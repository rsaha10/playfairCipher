userInput = input("Please input whether you would like to encode or decode, followed by ciphertext or plaintext, and lastly your desired keytext: ").upper()

x = userInput.split()
ED = x[0]
text = x[1]
key = None

if len(x) < 3:
    key = None
else:
    key = x[2]


def newKey():
    global userKey
    print("(note: key must contain all letters a-z only once, and characters ',' '.' ' ') PLEASE")
    userKey = input('enter the key you want to use: ')


def encode():
    listOfIndexes = []
    textToEncode = input('enter the text you want to encode: ')
    for char in textToEncode:
        listOfIndexes.append(defaultKey.index(char))
    for i in range(len(listOfIndexes)):
        listOfIndexes[i] = userKey[listOfIndexes[i]]
    encodedText = ''.join(listOfIndexes)
    print("\nkey: ",userKey,"\ntext you're encoding: ",textToEncode,"\nencoded text: ",encodedText,"\n")

def decode():
    listOfIndexes = []
    textToDecode = input("enter the text you want to decode: ")
    for char in textToDecode:
        listOfIndexes.append(userKey.index(char))
    for i in range(len(listOfIndexes)):
        listOfIndexes[i] = defaultKey[listOfIndexes[i]]
    decodedText = ''.join(listOfIndexes)
    print("\nkey: ",userKey,"\ntext you're decoding: ",textToDecode,"\ndecoded text: ",decodedText,"\n")



defaultKey = "abcdefghijklmnopqrstuvwxyz,. "
print("ENTER CORRESPONDING NUMBER\n")
while True:
    option = int(input("1) Enter the key. \n2) Encode with key. \n3) Decode with key.\n4) Exit program.\n"))
    if option == 1:
        newKey()
    elif option == 2:
        encode()
    elif option == 3:
        decode()
    elif option == 4:
        break
    else:
        print('invalid entry')

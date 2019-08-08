crypto= {   'A':'Z', 'B':'Y',
            'C':'X', 'D':'W', 'E':'V',
            'F':'U', 'G':'T', 'H':'S',
            'I':'R', 'J':'Q', 'K':'P',
            'L':'O', 'M':'N', 'N':'M',
            'O':'L', 'P':'K', 'Q':'J',
            'R':'I', 'S':'H', 'T':'G',
            'U':'F', 'V':'E', 'W':'D',
            'X':'C', 'Y':'B', 'Z':'A',
            '1':'0', '2':'9', '3':'8',
            '4':'7', '5':'6', '6':'5',
            '7':'4', '8':'3', '9':'2',
            '0':'1', ', ':'.', '.':',',
            '?':'/', '/':'?', '-':'-',
            '(':').', ')':'('}

print("Welcome to the program that makes encryption and decrypting according to Crypto code !!!")
keys="a"
while keys =="a":
    select=input("Press 1 to perform encryption, press 2 to decrypt. For quit 'q':").upper()
    if select == "Q":
        quit()
    elif select == "1":
        message= input("Please Typing Letter that you want to encrypt:").upper()
        crypto2= ""
        for letter in message:
            if letter !=" ":
                crypto2+= crypto[letter]
            else:
                crypto2+=" "
        print(crypto2)
    elif select== "2":
        message= input("Please Typing Letter that you want to decrypt:").upper()
        decrypt = ""
        lisst=list(crypto.items())
        for letter in message:
            for i in lisst:
                if letter == i[1]:
                 decrypt += i[0]
        print(decrypt)
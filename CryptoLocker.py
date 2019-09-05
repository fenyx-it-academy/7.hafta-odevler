import time

encryption_key = {'a': chr((ord('a')+20)*3), 'b': chr((ord('b')+20)*3), 'c': chr((ord('c')+20)*3),
                  'd': chr((ord('d')+20)*3), 'e': chr((ord('e')+20)*3), 'f': chr((ord('f')+20)*3),
                  'g': chr((ord('g')+20)*3), 'h': chr((ord('h')+20)*3), 'i': chr((ord('i')+20)*3),
                  'j': chr((ord('j')+20)*3), 'k': chr((ord('k')+20)*3), 'l': chr((ord('l')+20)*3),
                  'm': chr((ord('m')+20)*3), 'n': chr((ord('n')+20)*3), 'o': chr((ord('o')+20)*3),
                  'p': chr((ord('p')+20)*3), 'q': chr((ord('q')+20)*3), 'r': chr((ord('r')+20)*3),
                  's': chr((ord('s')+20)*3), 't': chr((ord('t')+20)*3), 'u': chr((ord('u')+20)*3),
                  'x': chr((ord('x')+20)*3), 'w': chr((ord('w')+20)*3), 'v': chr((ord('v')+20)*3),
                  'y': chr((ord('y')+20)*3), 'z': chr((ord('z')+20)*3),
                  '1': chr((ord('1')+20)*3), '2': chr((ord('2')+20)*3), '3': chr((ord('3')+20)*3),
                  '4': chr((ord('4')+20)*3), '5': chr((ord('5')+20)*3), '6': chr((ord('6')+20)*3),
                  '7': chr((ord('7')+20)*3), '8': chr((ord('8')+20)*3), '9': chr((ord('9')+20)*3),
                  '0': chr((ord('0')+20)*3), ',': chr((ord(',')+20)*3), '.': chr((ord('.')+20)*3),
                  '?': chr((ord('?')+20)*3), '/': chr((ord('/')+20)*3), '-': chr((ord('-')+20)*3),
                  '(': chr((ord('(')+20)*3), ')': chr((ord(')')+20)*3), ' ': chr((ord(' ')+20)*3),
                  '\'': chr((ord('\'')+20)*3)}


def Encryptor(text, en_key):
    encrypted_text = ''
    for i in text:
        encrypted_text += en_key[i]
    return encrypted_text


def Decryptor(text, en_key):
    decrypted_text = ''
    for i in text:
        if i in en_key.values():
            for k,v in en_key.items():
                if i == v:
                    decrypted_text += k
                    break
        else:
            decrypted_text += ' '
    return decrypted_text


while True:
    action = input("""\n\nPlease choose an action from the following menu;
To encrypt a text, press '1'
To decrypt a text, press '2'
To exit the program, press 'q'
Enter your choice: """)
    if action == "1":
        try:
            plain_text = input("\nPlease enter the text you would like to encrypt:\n").lower().rstrip('\r\n')
            encrypted_text = Encryptor(plain_text, encryption_key)

            print("\n\nThe text you entered is enrypted as follows:\n")
            letter_counter = 0
            for i in encrypted_text:
                if letter_counter == 121:
                    print('\n')
                    print(i, sep='', end='')
                    letter_counter = 0
                else:
                    print(i, sep='', end='')
                    letter_counter += 1
            time.sleep(6)
            print('\n\n')
        except KeyError:
            print('You must only enter letters, numbers of punctuation marks from the English alphabet!'
                  '\nTry again!')

    elif action == "2":
            encrypted_text = input("\nPlease enter the text you would like to decrypt:\n").rstrip('\r\n')
            decrypted_text = Decryptor(encrypted_text, encryption_key)

            print("\n\nThe text you entered is decyrpted as follows:\n")

            letter_counter = 0
            for i in decrypted_text:
                if letter_counter == 121:
                    print('\n')
                    print(i, sep='', end='')
                    letter_counter = 0
                else:
                    print(i, sep='', end='')
                    letter_counter += 1

            time.sleep(6)
            print('\n\n')

    elif action == "q":
        print('\nExiting the program....')
        time.sleep(3)
        quit()
print("*"*15,"ENCIPHERING SYSTEM","*"*15)
import random

characters = ["=","-","."]
let_num_cha = "qwertyuiopasdfghjklzxcvbnm1234567890<>?:\"|{}+_)(*&^%$#@!~,./;'[]=-`"
enciphering = {}

for let in let_num_cha:
    for cha in characters:
        if cha not in enciphering.values():
            enciphering[let] = cha
        else:
            for i in characters:
                cha += i
                if cha not in enciphering.values():                 #do same process as first if block
                    enciphering[let] = cha
                else:
                    cha += i
                    if cha not in enciphering.values():             # do same process as first if block
                        enciphering[let] = cha
                    else:
                        for i in characters:
                            cha += i
                            if cha not in enciphering.values():     # do same process as first if block
                                enciphering[let] = cha

for i in enciphering.items():
    print(i)



print("""
You can choose options below which you want:
-Press 1 to encipher a text
-Press 2 to make a text from enciphering
-Press q to quit\n""")
try:
    while True:
        replying = input("Enter your precession:")

        if replying == "1":
            text = input("Please enter your text to encipher:")
            encipher_text = ""
            for letter in text.lower():
                if letter != " ":
                    encipher_text += enciphering[letter] + " "
                else:
                    encipher_text += " "
            print("--------->",encipher_text,"\n")

        elif replying == "2":
            enciphered_text = input("Please enter your enciphered text to make a text:")
            enciphered_text += " "                              #add a space to make words correctly
            make_letter = ""                                    #to add enciphering here in order to find its letter situation
            make_text = ""                                      #to add letters
            for enc in enciphered_text.lower():
                if enc != " ":
                    n = 0                                       #set a 'n' variable to make text correctly according to space
                    make_letter += enc
                else:
                    n += 1
                    if n == 2:
                        make_text += " "
                    else:
                        make_text += list(enciphering.keys())[list(enciphering.values()).index(make_letter)]  # to find the letter according to enciphering
                        make_letter = ""
            print(f"Your text is '{make_text}'\n")

        elif replying.lower() == "q":
            break

        else:
            print("please enter options above\n")

except ValueError:
    print("Your enter is wrong,please try again")
except:
    print("Something happened wrong, please try again")

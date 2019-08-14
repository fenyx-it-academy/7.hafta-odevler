print("********** Cryptography Program *********\n\n\n")
print("Welcome to the Cryptography Program.")
crypto_code={"a":"α", "b":"β", "g":"γ",
                "d":"δ", "e":"ε", "z":"ζ",
                "h":"η", "t":"θ", "i":"ι",
                "k":"κ","l":"λ", "m":"μ",
                "n":"ν", "x":"ξ", "o":"ο",
                "p":"π", "r":"ρ", "s":"σ",
                "v":"τ", "u":"u", "f":"φ",
                "c":"χ", "j":"ψ", "q":"ω",
                "w":"ш","y":"й",
                '1':'٥', '2':'٤', '3':'٨',
                '4':'١', '5':'.', '6':'٩',
                '7':'٢', '8':'٣', '9':'٧',
                '0':'Z', ',':'$', '.':'#',
                '?':'£', '/':'*', '-':'/',
                '(':'<', ')':'>'}
while True:
    operation=input("""Please choose a operation you would like to do;
For encryption, press      "1"
For decryption, press      "2"
To exit the program, press "q"
""")
    if operation =="1":
     while True:
      try:
        data=input("Please enter the data you would like to encrypt.\n")
        crypto=""
        for i in data.lower():
            if i !=" ":
                crypto+=crypto_code[i]
            else:
                crypto+=" "
        print("This is the encrypted version of the data: ",crypto,"\n")
        break
        continue
      except KeyError:
          print("You made an incorrect entry. Please enter the data with only English character.")
          q=input("""Would you like to quit? If yes please press "q", if no please press "ENTER".
""")
          if q.lower()=="q":
             print("Program terminated.")
             exit()
          elif not q:
             continue
            
    elif operation.lower()=="q":
        print("Program terminated.")
        exit()
    elif operation=="2":
     while True:
      try:
        data=input("Please enter the data you would like to decrypt.\n")
        key=list(crypto_code.keys())
        value=list(crypto_code.values())
        decrypto=""
        for i in data:
            if i !=" ":
                decrypto+=key[value.index(i)]
            else:
                decrypto+=" "
        print("This is the decrypted version of the data:",decrypto,"\n")
        break
        continue
      except ValueError:
         print("You made an incorrect entry. Please enter the data with only crypted character.")
         q=input("""Would you like to quit? If yes please press "q", if no please press "ENTER".
""")
         if q.lower()=="q":
             print("Program terminated.")
             exit()
         elif not q:
             continue
    else:
        print("You entered an incorrect operation code. Please check and read instructions.")
        continue

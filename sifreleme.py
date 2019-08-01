print("SIFRELEME PROGRAMI")

kodlama = {"A":"Q",
           "a":"q",
           "B":"W",
           "b":"w",
           "C":"E",
           "c":"e",
           "Ç":"Ş",
           "ç":"ş",
           "D":"R",
           "d":"r",
           "E":"T",
           "e":"t",
           "F":"Y",
           "f":"y",
           "G":"U",
           "g":"u",
           "Ğ":"Ü",
           "ğ":"ü",
           "H":"I",
           "h":"ı",
           "I":"O",
           "ı":"o",
           "İ":"Ğ",
           "i":"ğ",
           "J":"P",
           "j":"p",
           "K":"A",
           "k":"a",
           "L":"S",
           "l":"s",
           "M":"D",
           "m":"d",
           "N":"F",
           "n":"f",
           "O":"G",
           "o":"g",
           "Ö":"İ",
           "ö":"i",
           "P":"H",
           "p":"h",
           "Q":"J",
           "q":"j",
           "R":"K",
           "r":"k",
           "S":"L",
           "s":"l",
           "Ş":"Ç",
           "ş":"ç",
           "T":"Z",
           "t":"z",
           "U":"X",
           "u":"x",
           "Ü":"Ö",
           "ü":"ö",
           "V":"C",
           "v":"c",
           "W":"V",
           "w":"v",
           "X":"B",
           "x":"b",
           "Y":"N",
           "y":"n",
           "Z":"M",
           "z":"m",
           " ":">",
           "1":"5",
           "2":"4",
           "3":"9",
           "4":"6",
           "5":"2",
           "6":"8",
           "7":"1",
           "8":"3",
           "9":"0",
           "0":"7",
           ".":";",
           ":":"@",
           ",":"!",
           "(":"*",
           ")":"-",
           "?":"+"}
while True:
    menu = input("""    1- Sifreleme
    2- Desifreleme
    3- Cikis
    
    Yapmak istediginiz islemin numarasini giriniz :""")

    if menu=="1":
        metin_sifreli=""
        metin = input("Lutfen sifrelemek istediginiz metni giriniz :")
        for i in metin:
            metin_sifreli += kodlama[i]
        print("""\n METNINIZ >>> {} <<< OLARAK SIFRELENMISTIR. \n """.format(metin_sifreli))

    elif menu=="2":
        metin_cozum=""
        liste = list(kodlama.items())

        
        metin_sifreli=input("Lutfen desifre yapmak istediginiz metni giriniz :")
        for a in metin_sifreli:
            for b in liste:
                if a==b[1]:
                    metin_cozum+=b[0]
        print("""\n SIFRENIZ >>> {} <<< OLARAK DESIFRE EDILMISTIR \n""".format(metin_cozum))

    elif menu=="3":
        quit()
    else:
        print("\n**** Lutfen gecerli menu numarasi giriniz...!!! **** \n")
        continue
        

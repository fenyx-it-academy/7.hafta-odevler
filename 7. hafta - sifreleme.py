#Sifreleme Odevi:
##Şifreleme Uygulaması
##Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve
##sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz. 
##Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve
##kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin 
##ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input
##olarak yazdiginda orjinal metne ulasabilsin.
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
print("""
              Mors Alfabesiyle            
        sifreleme ve desifreleme islemi      
                yapmak icin;

               Hosgeldiniz!!!

               1- Sifreleme 
               2- Desifreleme
               
               3- Cikis
               
          .
               
""")
while True:
    secim = input("\nYapmak istediginiz islemi seciniz: ")

    if secim =="3":
        print("Cikiliyor...")
        quit()

    if secim == "1":
        mesaj = input("Lutfen sifrelemek istediginiz kelimeyi giriniz: ").upper()
        sifre = ""
        for harf in mesaj:
            if harf != " ":
                sifre += MORSE_CODE_DICT[harf] + " "       
            else:
                sifre += " "
        print("\n",mesaj,"kelimesinin sifrelenmis hali: ",sifre)

    if secim == "2":
        mesaj = input("\nLutfen cozmek istediginiz sifreyi giriniz: ")
        mesaj += " "
        desifre = ""
        mors_kar = ""

        for harf in mesaj:
            i = 0
            if harf != " ":
                mors_kar += harf
            else:
                i += 1 
                if i == 2:
                    desifre += " "            
                else:
                    desifre += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mors_kar)]
                    mors_kar = ""

        print("\n",mesaj,"sifresinin desifre edilmis hali: ",desifre)

        
        

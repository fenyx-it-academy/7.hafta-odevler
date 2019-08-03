#Bu online dersten alinan iceriktir.
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
print("\nMors alfabesine gore sifreleme ve desifreleme islemi yapan programa hosgeldiniz!!!\n")
while True:
    secim = input("Sifreleme islemi yapmak icin 1'e basiniz, desifreleme islemi yapmak icin de 2'ye basiniz.")

    if secim == "1":
        mesaj = input("Lutfen sifrelemek istediginiz metni giriniz:\n").upper()
        sifre = ""
        for harf in mesaj:
            if harf != " ":
                sifre += MORSE_CODE_DICT[harf] + " "       
            else:
                sifre += " "
        print(sifre)

    if secim == "2":
        mesaj = input("Lutfen sifresini cozmek istediginiz kodu giriniz:\n")
        mesaj += " "
        desifre = ""
        mors_kar = ""

        for harf in mesaj:
            if harf != " ":
                i = 0
                mors_kar += harf
            else:
                i += 1 
                if i == 2:
                    desifre += " "            
                else:
                    desifre += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mors_kar)]
                    mors_kar = ""

        print(desifre)

        
        

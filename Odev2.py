##Şifreleme Uygulaması (Vigenere Şifreleme)
##Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli metni
##orjinal metne donusturebilen bir program yazmanizi istiyoruz. 
##Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan
##alacaginiz inputu bu algoritma yoluyla sifreleyin 
##ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input olarak
##yazdiginda orjinal metne ulasabilsin.

sozluk={'A':1, 'B':2, 'C':3, 'D':4, 'E':5,
        'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
        'K':11, 'L':12, 'M':13, 'N':14, 'O':15,
        'P':16, 'R':17, 'Q':18, 'S':19, 'T':20,
        'U':21, 'X':22, 'V':23, 'W':24, 'Y':25,
        'Z':26, '.':27, ',':28, '?':29, '!':30,
        '-':32, '_':33, '@':34, " ":35, '1':36,
        '2':37, '3':38, '4':39,'5':40, '6':41,
        '7':42, '8':43, '9':44, '0':31, "'":0}                                          # harfler, rakamlar ve bazi noktalama isaretleti iceren sozluk olusturuldu.
sifreleme = ""                                                                          # ve hepsine bir rakamsal deger verildi.
desifreleme = ""                                                                        # bos diziler olusturuldu.
anahtar = 2                                                                             # bir degisken olusturuldu.
print(""" *** Hosgeldiniz ***   """.center(50))
while True:
    sec = input("Sifreleme yapmak icin 1'e,\nDesifreleme yapmak icin 2'ye,\
                 \nCikmak icin q'ya basiniz:").lower()                                  # kullanicidan ne yapmak istedigi soruldu.
    print("\n")
    if sec == "1":                                                                      
        metin = input("Lutfen sifrelemek istediginiz metni yaziniz:\n")                 # sifrelenecek metin istendi.
        for harf in metin.upper():                                                      # metindeki her harf for ile harf'de depo edildi.
            if harf != " ":                                                             # harf bosluga esit deilse if blogu calistirildi.
                deger = (int(sozluk[harf])+anahtar)%44                                  # harfin sozlukdeki degeri anahtar ile toplandi ve 44 ile bolumunden kalan deger degiskenine atandi.
                anahtar += 2                                                            
                son_deger = list(sozluk.keys())[list(sozluk.values()).index(deger)]     # sozlukdeki values liste yapildi ve index(deger) hafizada tutuldu,  
                print(son_deger,end="")                                                 # sonra bu hafizada tutulan yeni deger keys listesinde hangi index ise o harf ekrana yazdirildi.
            elif harf == " ":                                                           # for ile alinan harfler bosluga denk gelir ise bir bosluk birakildi.
                print(" ",end="")                                                       # kelimeleri ayirmak icin.
        print("\n")
        anahtar=2                                                                       # anahtar tekrar ikiye esitlendi desifre yaparken ayni islem geri calisabilsin diye.
    elif sec == "2":
        metin = input("Lutfen desifrelemek istediginiz metni yaziniz:\n")
        for harf in metin.upper():
            if harf != " ":
                deger = (int(sozluk[harf])-anahtar)%44
                anahtar +=2
                son_deger = list(sozluk.keys())[list(sozluk.values()).index(deger)]
                print(son_deger, end="")
            elif harf == " ":
                print(" ", end="")
        print("\n")
        anahtar=2
    elif sec == "q":
        print("program kapatiliyor...")
        quit()
    else:
        print("Lutfen '1' , '2' veya 'q' seciniz!!!\n")
        continue

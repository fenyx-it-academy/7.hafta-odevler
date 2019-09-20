# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:30:49 2019

@author: HP
"""

#Şifreleme Uygulaması ;
#Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli metni orjinal metne donusturebilen 
#bir program yazmanizi istiyoruz.Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan 
#alacaginiz inputu bu algoritma yoluyla sifreleyin ve ekrana yazdirin. 
#Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal metne ulasabilsin.

print("""\nOrijinal metni sifreli metne ve sifreli metni orijinal metne donusturme islemi yapan 
                          programa hosgeldiniz!!!\n""")
Sozluk = {'A':'0',  'B':'1',   'C':'2',  'D':'3',  'E':'4',  'F':'5',  'G':'6',  'H':'7',
          'I':'8',  'J':'9',   'K':'10', 'L':'11', 'M':'20', 'N':'40', 'O':'12', 'P':'21', 'Q':'39',
          'R':'13', 'S':'22',  'T':'38', 'U':'14', 'V':'23', 'W':'37', 'X':'15', 'Y':'24', 'Z':'36',
          '1':'16', '2':'25',  '3':'35', '4':'17', '5':'26', '6':'34', '7':'18', '8':'27', '9':'33',
          '0':'19', ', ':'28', '.':'32', '?':'41', '/':'29', '-':'31', '(':'42', ')':'30'}
while True:
    secim = input("""Orijinal metni sifrelemek icin 1'e basiniz (Sifreleme)),
sifreli metni orijinal metne donusturmek icin de 2'ye basiniz(Desifreleme),
Cikmak icin lutfen 3 e basiniz... ; """)
    
    # Orijinal ==> Sifreli .................
    if secim == "1":
        metin = input("Lutfen  metni giriniz:").upper()
        sifrele = ""
        for i in metin:
            if i != " ":
                sifrele += Sozluk[i] + " "
            else:
                sifrele += " "
        print(sifrele)
                
    # Sifreli ==> Orijinal .................    
    elif secim == "2" :
        metin = input("Lutfen  metni giriniz:")
        metin += " "
        desifre = ""
        harfdiz = ""

        for harf in metin:
            if harf != " ":
                i = 0
                harfdiz += harf
            else:
                i += 1
                if i == 2:
                    desifre += " "
                else:
                    desifre += list(Sozluk.keys())[list(Sozluk.values()).index(harfdiz)]
                    harfdiz = ""
        print(desifre)
        
    else :
        print("cikiliyor...")
        break
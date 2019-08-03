#aciklama yapiyorum.

print('''
                 SIFRELEME PROGRAMI
Bu programda harfler belli bir algoritmaya gore sifrelenmistir.
*Orjinal metinden sifreli metine gecmek icin 1'e
*Sifreli metinden orjinal metne gecmek icin 2'ye
*Cikmak icin 3'e basiniz.
''')


#oncelikle iki veri grubu belirliyorum.Ilki asil harlerim ikincisi de anahtarim.
#bunlari tuple olarak sectim cunku sirasi bozulmadan birbiriyle esletirecegim.
keys=tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
value=tuple("KLMNOPQRSTUVWXYZABCDEFGHIJ567891234")
#anahtar olarak kullanacagim bir sozluk olusturuyorum.Bosluk icinde 0 in kullanilmasini
#tanimliyorum. Bir bos bir string tanimliyorum. Sifreli metini olusturmak icin.
anahtar={" ":0}
ters_anahtar={" ":0}
metin=""
ters_metin=""
#iki tuple i kullanarak bir sozluk oluturuyorum.
while True:
    
    giris=(input("Seceneginiz: "))
    
    if giris=="3":
        print("Cikis yapiliyor..")
        break

    elif giris=="1":
        orjinal=input("Orjinal metni giriniz: ")
        
        for i in keys:
            for k in value:
                if keys.index(i)==value.index(k):
                    anahtar[i]=k
        print(anahtar)

#orjinal metini istiyorum.
        

#her ihtimale karsi elemanlari buyuk harfe ceviriyorum.
#daha sonra girdigim elemanlari anahtar ustunde taratip karsilik gelen
#harfi METINE EKLEMEYE CALISIYORUM AMA OLMUYOR.
        for i in orjinal.upper():
    
            yeni_metin=metin+anahtar[i]
            print(yeni_metin)
#ayni islemi kriptolanmis bir metin icin yapiyorum.
    elif giris=="2":
        
        kripto=input("Metnin sifrelenmis halini giriniz: ")
        
        for i in value:
            for k in keys:
                if value.index(i)==keys.index(k):
                    ters_anahtar[i]=k

        print(ters_anahtar)

        for i in kripto.upper():
            
            orj_metin=ters_metin+ters_anahtar[i]
            
            print(ters_anahtar[i])
#yanlis bir veri girisi durumunda uyariyorum.
    else:
        print("Yanlis bir veri girisi yaptiniz.Lutfen tekrar deneyiniz.")
            






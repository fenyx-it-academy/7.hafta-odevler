
#----------SIFRELEME KARAKTERLERI----------------------------

alfabe='QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç1234567890.,:!/? \n'
a=0
sozluk={}
liste=[]
for i in range(1):

    for sayac in alfabe:
        a+=1

        sozluk[sayac]=str(bin(a+4)[2:].zfill(7))

for k,d in sozluk.items():
    liste+=[k,d]
  #---------------KODLAMA BINARY OLARAK 1 DEN BASLAYAN SAYILARA 4 EKLEMEK SURETIYLE 7 BIT KODLANDI
  #BOSLUK VE (ENTER) TUSUDA KODLANDIGI ICIN YANYANA GORUNEN (101010111) GIBI BIR KOD GOZUKUYOR

print(liste)
print(""""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        KODU SIFRELEME
1- ILK SATIRI GECMEYECEK SEKILDE METIN GIRILIR (ENTER) 'E BASILIR VE SIFRELENIR.
2- OLUSTURULMUS OKUMA.TXT'E DOSYASINA CEVIRMEK ISTEDIGINIZ UZUN METNI GIRINIZ VE (ENTER)'E BASINIZ

                        KOD COZME
1- COZMEK ISTEDIGINIZ SIFRELI METNI GIRINIZ OTOMATIK CEVIRILIR
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")

#UZUN METINLERI SIFRELEME YAPMAK ICIN DOSYADAN YARALANACAGIZ
with open("okuma.txt",'a', encoding="cp1254") as oku:
    oku.write('')

while True:
    #----------------SECME INPUTLARI----------------------
    secme=input("""
_________SIFRELEME PROGRAMINA HOS GELDINIZ___________
    SIFRELEME      (1)   UZUN METIN SIFRELEME  (11)
    SIFRE COZUCU   (2)              CIKIS (Q)
------------------------>>:""").upper()
    if secme=='Q':
        print('cikiliyor')
        break
    #---INPUT KOMUTU TEK SATIR ALDIGI ICIN ELLE GIRIS YAPILIR TEK SATIR YAZILIR----
    elif secme=='1':
        metin_1=input('metni giriniz:')
        sifrele=""

        for harf in metin_1:

           if harf not in sozluk:
               sifrele+=sozluk['?'] # OLMAYAN KARAKTERLERE ? KOYAR
               continue
           else:
               sifrele+=sozluk[harf]
        print('\n')
        print(sifrele,end='')

        continue
    #----UZUN METINLERI SIFRELEMEK ICIN BU KISIM KULLANILIR----------
    elif secme=="11":
        metin_11=input("Dosyaniza cevirilecek metni girin ve (ENTER )'e basin")
        with open ( "okuma.txt" , 'r+',encoding="cp1254") as oku :
            okuma=oku.read() #DOSYAYA METIN EKLEMENIZ YETERLIDIR
            sifrele_2 =""""""
            print(okuma)
            for harf in okuma :
                if harf not in sozluk :
                    sifrele_2+= sozluk['?']
                    continue
                else:
                     sifrele_2 += sozluk[harf]
            print ( '\n' )
            print ( sifrele_2 ,end='')
        continue
    #--------------SIFRELEME KISMI-------------------------

    elif secme=='2':

        metin_2=input("""cozulecek metni giriniz"""'\n')
        coz=""""""
        depo=""
        say=0

        for kod in metin_2:#SIFRELEME HER KARAKTERE 7 BIT VERDIGI ICIN 7BITLIK OKUMA YAPIYOR
            say+=1         #BUTUN BITLERI YANYANA YAZIYOR
            depo+=kod
            if say ==7:
                if depo in liste:
                    coz+=liste[liste.index(depo)-1]
                    depo=""
                    say=0

        print('\n')
        print(coz,end='')
        coz=''

        continue
    else:
        print('yanlis tusa bastiniz')
        continue

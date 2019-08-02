##Şifreleme Uygulaması
##Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli
##metni orjinal metne donusturebilen bir program yazmanizi istiyoruz. 
##Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan
##alacaginiz inputu bu algoritma yoluyla sifreleyin ve ekrana yazdirin.
##Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal
##metne ulasabilsin.

## Belirli sayida eleman iceren bir kume olusturuldu. Sifreleme icin listenin disina cikmayiniz!!

liste={'a':'9','b':'8','c':'7','d':'6','e':'5','f':'4','g':'3','h':'2','k':'1','l':'0'}	
liste_keys=[]
liste_values=[]                         ## anahtar ve degerler iki ayri listede toplandi
liste_keys += liste.keys()
liste_values += liste.values()
print(liste_keys)
print(liste_values)    
sifre=[]
print("\n")
print(""" Lutfen asagidaki islemlerden birini seciniz:

            1- Metin sifrelemek

            2- Sifre cozmek"""    )

import random 

kul1=input("Tercihiniz : ")

if kul1 == "1":

    kul2=input(" Sifrelemek istediginiz metni giriniz: ")

    for i in kul2:
        try:
            sifre=liste.get(i)                         ## metindeki elemanlara tekabul eden degerler sifre adli listede toplandi 
            if i not in sifre:
                print(sifre,end="")
        except:
                print(">>>","Lutfen sadece listeden harf seciniz!!!") 
if kul1 == "2":

    kul3=input("Sifrenizi giriniz ; ")
    
    for i in kul3:
        try:
            metin= list(liste.keys())[list(liste.values()).index(i)]   ##uzun hikaye:-)
            print(metin, end="")
        except:
            if len(kul3)==1:
                print(" >>>","sadece rakam giriniz!!!")


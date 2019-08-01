#Şifreleme Uygulaması
#Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz. 
#Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin 
#ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal metne ulasabilsin.




alfabe= {"a":"562" , "b":"658" , "c":"78",
          "ç":"39" ,  "d":"63" , "e":"478",
          "f":"24" , "g":"07" , "ğ":"17",
          "h":"69" , "ı":"0" , "i":"10",
          "j":"99" , "k":"52" ,"l":"06",
          "m":"09" , "n":"571" , "o":"61",
          "ö":"30" , "p":"26" , "r":"3",
          "s":"23" , "ş":"85" , "t":"661",
          "u":"965" , "ü":"1" , "v":"123" , "y":"321" , "z":"231",
          "1":"+-*/" , "2":"-+*/" , "3":"*-+/",
          "4":"*+-/" , "5":"/*-+" ,"6":"*/-+",
          "7":"/+*-" , "8":"+-/*" , "9":"+*-/" , "0":"/-*+",
          ",":"--" ,  ".":"++" , "?":"-+" , "/":"+-" , "-":"**" , "(":"*+" ,  ")":"*-"}
print("\nyeni alfabe  gore sifreleme ve şifreli metni orjinal metne çevirme  islemi yapan programa hosgeldiniz!!!\n")
secenek = ("Sifreleme islemi yapmak icin 1'e basiniz\n şifreli metni orjinel metne çevirmek icin de 2'ye basiniz\nçıkmak için 3'e basınız.\n")
print(secenek)
while True:
    secim = input("seciminiz:")
    if secim == "1":
        mesaj = input("Lutfen sifrelemek istediginiz metni giriniz:\n").lower()
        metin = ""
        keys=alfabe.keys()
        for harf in mesaj:
            if harf !=" ":
                metin += alfabe[harf] +" "
            else:
                if not harf in metin:
                    print("yanlış kodlama yaptınız...")
                    break
                else:
                    metin += ""
        else:
            print(metin)
    if secim == "2":
        kod = input("Lutfen sifresini cozmek istediginiz kodu giriniz:\n").lower()
        kod += " "
        çözülen = ""
        a = ""
        values=alfabe.values()
        for harf in kod:
            if harf != " ":
                i = 0
                a += harf
            else:
                i += 1 
                if i == 2:
                    çözülen += "\t "
                else:
                    if not a in values:
                        print("yanlış kodlama yaptınız..")
                        break
                    else:
                        çözülen+= list(alfabe.keys())[list(alfabe.values()).index(a)]
                        a = ""
        else:
            print(çözülen)
    if secim=="3":
        çıkış=input("çıkmak için q'ya basınız:")
        if çıkış=="q":
            print("çıkılıyor..")
            break
        else:
                print("yanlış seçim tekrar seçiniz..")
                continue
                
    
            
        
        

bilgi = """
SIFRELEME PROGRAMI
1. deşifreli metni şifreliye cevir
2. şifreli metni deşifreye cevir
3. Cikis 
"""
liste = []
for i in range(128):
    karakter = "%c" % i
    liste += [karakter]
sifre = dict()
for i in range(len(liste)):
    sifre[liste[i]] = chr(ord(liste[i]) + 5)

şifreli = ""
deşifreli = ""
while True:
    print(bilgi)
    secimm = input("Seciminiz: ")
    şifreli = ""
    if secimm == "1":
        metin = input("deşifreli metin: ")
        for i in metin:
            şifreli += sifre[i]
        print("Metnin sifreli hali  :", şifreli)

    elif secimm == "2":
        metin = input("şifreli metin giriniz: ")
        deşifreli = ""
        for i in metin:
            for k, v in sifre.items():
                if i == v:
                    deşifreli += k
        print("Metnin deşifrelisi  :", deşifreli)
    elif secimm == "3":
        print("Cikis yapiliyor...")
        break
    else:
        print("Yanlis giris yaptiniz..")
        break

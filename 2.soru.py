# Şifreleme Uygulaması
# Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz.
# Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin
# ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal metne ulasabilsin.

cikti = """
SIFRELEME PROGRAMI
1. Orjinal metni sifreye cevir
2. Sifreli metni orjinale cevir
3. Cikis 
"""
liste = []
for i in range(128):  # ascii de 128 karaktere kadar oldugu icin
    karakter = "%c" % i
    liste += [karakter]  # listeye ascii kodlarindaki tum karakterler atildi
sifre = dict()  # sifrelemenin yapilacagi sozlugu tanimla
for i in range(len(liste)):
    sifre[liste[i]] = chr(ord(liste[i])+5)
    # sifre ascii kod decimal karsiliklarinin 5 fazlasina karsilik gelen karakter

sifreli = ""
orjinal = ""
while True:
    print(cikti)
    secimm = input("Seciminiz: ")
    sifreli = ""  # her seferinde degeri bosaltildi
    if secimm == "1":
        metin = input("Orjinal metin: ")
        for i in metin:  # orjinal metin taraniyo
            # sozlukte karaktere karsilik gelen degeri sifreli stringine atiliyo
            sifreli += sifre[i]
        print("Metnin sifreli hali  :", sifreli)  # yazdiriliyor

    elif secimm == "2":
        metin = input("Sifrelenmis metni giriniz: ")  # sifreli metni alindi
        orjinal = ""  # her seferinde degeri bosaltiyorm
        for i in metin:  # sifreli metni tariyorm
            for k, v in sifre.items():  # sozlukteki key ve value degerini aldk
                if i == v:  # eger sifreli metindeki karakter sozlukte karsilik gelen value degerine esitse
                    orjinal += k  # orjinal stringine anahtar degerini atiyor
        print("Metnin orjinali  :", orjinal)  # dongu bitince yazdiriyoruz
    elif secimm == "3":
        print("Cikis yapiliyor...")
        break
    else:
        print("Yanlis giris yaptiniz..")
        break

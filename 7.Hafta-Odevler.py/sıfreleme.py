""""Şifreleme Uygulaması
Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz.
Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin
ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal metne ulasabilsin.
"""

secenek = """yapmak istediginiz islemi secin
(1) orijinal metni sifreli metne cevir
(2)sifreli metni original metne cevir
(q) cikis"""

sifre = {"1.A":0, "2.A":3,"3.A":6,"4A.":9}
original = "sifreniz adimlardan olusmaktadir.o dan baslayip 3 er artmakta 9 ile bitmektedir "
while True:
    try:
        islem = input("yapmak istediginiz islemi secin: ")
        if islem == "1":
            print(sifre.keys())
        elif islem == "2":
            for keys,value in sifre.items():
                print(original,"{} = {}".format(keys,value))
        elif islem == "q":
            break
        else:
            print("boyle bir secenek yok.tekrardeneyin")
    except:
        print("bir hata olustu")
secenek="""Bu Bir Sifreleme Programidir
Lutfen yapmak istediginiz islemi seciniz
Metni Sifrelemek Icin :             1
Sifreli Metni Cozmek Icin :         2
Islemden cikmak icin    :           q
basiniz!!!!\n"""

birlerbasamagi = {
    "0":"3", "1":"5", "2":"7", "3":"9", "4":"0", "5":"2", "6":"1", "7":"6", "8":"4", "9":"8",
    "q":"m", "w":"n", "e":"b", "r":"v", "t":"c", "y":"x", "u":"z", "i":"l", "o":"k", "p":"j", "a":"h",
    "s":"g", "d":"f",
   "m":"q", "n":"w", "b":"e", "v":"r", "c":"t", "x":"y", "z":"u", "l":"i", "k":"o", "j":"p", "h":"a",
    "g":"s", "f":"d"
    }
src=list(birlerbasamagi.keys())
print(src)
print(type(src))
dst=list(birlerbasamagi.values())

while True:
    sonuc = ""
    secim = input(secenek)
    if secim=="1":
        metin=input("Sifrelemek istediginiz metni giriniz:")
        for i in metin:
            sira=src.index(i)
            kriptolu=dst[sira]
            sonuc+=kriptolu
            continue
        print("Sifrelenmis metniniz", sonuc)
        continue
    elif secim=="2":
        metin = input("Sifrelenmis metni giriniz:")
        for i in metin:
            sira = dst.index(i)
            kriptolu = src[sira]
            sonuc += kriptolu
            continue
        print("Metninizin sifrelenmemis hali", sonuc)
        continue
    elif secim=="q":
        quit()
    else:
        print("yanlis bir deger girdiniz")
        continue






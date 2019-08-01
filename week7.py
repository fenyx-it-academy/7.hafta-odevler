# telefon rehberi uygulamasi
# Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
# Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme,
# rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
# Olusturulan rehberi bir dosyaya kaydedin.
# Rehberi olustururken sozlukleri kullanin.


menu = ("""\nTELEFON REHBERIM

1. Rehbere isim ekle
2. Rehberden Kisi Sil
3. Rehber Guncelleme
4. Rehberi Listele
5. Cikis

""")
rehber = {}
while True:
    print(menu)
    secim = input("Seciminiz:\t")
    if secim == "1":
        print("Not: Rehberde ayni isimden baska biri varsa eklenmeyecektir.")
        ad_soyad = input("Rehbere eklemek istediginiz kisinin adi soyadi:")
        tel = input("Rehbere eklemek istedigini kisinin tel numarasi ")
        rehber[ad_soyad.lower()] = tel
        continue
    elif secim == "2":
        sil = (input("Silmek istediginiz kisinin adini-soyadini giriniz:")).lower()
        for k in rehber.keys():
            if k == sil:
                rehber.pop(sil)
                print(sil.upper(), " adli kisi silindi...")
                break
            else:
                print("Boyle bir ad-soyad bulunamadi..")
                break
        continue
    elif secim == '3':
        guncelle = (input("Guncellemek istediginiz \nKisinin adi soyadi ise 1,\nTelefon numarasi ise 2'ye basiniz: "))
        if guncelle == "1":
            ad_soyad = input("Rehberde guncellemek istediginiz kisinin adi soyadi:").lower()
            for k in rehber.keys():
                if k == ad_soyad:
                    tel = rehber[ad_soyad]
                    rehber.pop(ad_soyad)
                    ad_soyad2 = input("Guncel adi-soyadini giriniz: ").lower()
                    rehber[ad_soyad2] = tel
                    print("Basariyla guncellendi...\n")
                    break
                else:
                    print("Yanlis giris yaptiniz..\n")
                    break
            continue
        elif guncelle == "2":
            ad_soyad = input("Rehberde guncellemek istediginiz kisinin adi soyadi:").lower()
            for k in rehber.keys():
                if k == ad_soyad:
                    tel = input("Kisinin guncel tel numarasi: ")
                    rehber[ad_soyad] = tel
                    print("Basariyla guncellendi...\n")
                    break
                else:
                    print("Yanlis giris yaptiniz..\n")
                    break
            continue

    elif secim == '4':
        for k, v in rehber.items():
            print("\nAdi-Soyadi: {}\t\tTelefon Numarasi:{}".format(k.upper(), v))
    elif secim == "5":
        print("Cikis Yapiliyor...")
        break
    else:
        print("Yanlis secim yaptiniz lutfen tekrar deneyiniz...\n")
        continue

dosya = open("telefonrehberi.txt", "w")
dosya.write("Ad-Soyad\tTelefon Numarasi\n")
for k, v in rehber.items():
    a = "{}\t{}\n".format(k.upper(), v.upper())
    dosya.write(a)
dosya.close()


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
    liste += [karakter]  # listeye ascii kodlarindaki tum karakterleri attik
sifre = dict()  # sifrelemenin yapilacagi sozlugu tanimladik
for i in range(len(liste)):
    sifre[liste[i]] = chr(ord(liste[i])+5)
    # sifre ascii kod decimal karsiliklarinin 5 fazlasina karsilik gelen karakter

sifreli = ""
orjinal = ""
while True:
    print(cikti)
    secimm = input("Seciminiz: ")
    sifreli = ""  # her seferinde degeri bosaltiyoruz
    if secimm == "1":
        metin = input("Orjinal metin: ")
        for i in metin:  # orjinal metni tariyoruz
            # sozlukte karaktere karsilik gelen degeri sifreli stringine atiyoruz
            sifreli += sifre[i]
        print("Metnin sifreli hali  :", sifreli)  # yazdiriyoruz

    elif secimm == "2":
        metin = input("Sifrelenmis metni giriniz: ")  # sifreli metni aldik
        orjinal = ""  # her seferinde degeri bosaltiyoruz
        for i in metin:  # sifreli metni tariyoruz
            for k, v in sifre.items():  # sozlukteki key ve value degerini aldik
                if i == v:  # eger sifreli metindeki karakter sozlukte karsilik gelen value degerine esitse
                    orjinal += k  # orjinal stringine anahtar degerini atiyor
        print("Metnin orjinali  :", orjinal)  # dongu bitince yazdiriyoruz
    elif secimm == "3":
        print("Cikis yapiliyor...")
        break
    else:
        print("Yanlis giris yaptiniz..")
        break

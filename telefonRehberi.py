rehber = {}
rehberDosyasi = open("rehberDosyasi.txt", "a")
while True:
    print(" 1-rehbere kisi ekleme\n 2-kisi silme\n 3-kisi guncelleme\n 4-rehberi listele\n 5-cikis (kaydet)")
    secim = input("\t\t\tyapacaginiz islemi seciniz: ")

    if (secim == "1"):
        adSoyad = input("kisi adını giriniz ")
        telefonNumarasi = input("telefon numarasını giriniz")
        if adSoyad not in rehber:
            rehber[adSoyad] = telefonNumarasi
            print("kisi basarıyla eklendi")
        else:
            print("aynı isimde baskasi mevcut")

    elif (secim == "2"):
        kisi = input("silinecek kisinin adını giriniz")
        if kisi not in rehber:
            print("Böyle bir kisi yok")
        else:
            del rehber[kisi]
            print("kisi basarıyla silindi")

    elif (secim == "3"):
        adSoyad = input("güncellemek istediginiz kisi adını giriniz ")
        if adSoyad not in rehber:
            print("Böyle bir kisi mevcut degil")
        else:
            telefonNumarasi = input("yeni telefon numarasını giriniz")
            rehber[adSoyad] = telefonNumarasi
            print("kisi basarıyla güncellendi")

    elif (secim == "4"):
        for ad, numara in rehber.items():
            print(ad, numara)

    elif (secim == "5"):
        print("cikis yapılıyor, rehber dosyaya kaydediliyor")
        rehberDosyasi.write(str(rehber))
        break

    else:
        print("yanlış secim yaptınız, tekrar deneyiniz")


rehberDosyasi.close()
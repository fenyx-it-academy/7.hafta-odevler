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
        print("Not: Rehberde tekrarlayan isim olmamaktadir.")
        ad_soyad = input("Rehbere eklemek istediginiz kisinin adi soyadi:")
        tel = input("Rehbere eklemek istedigini kisinin tel numarasi ")
        rehber[ad_soyad.lower()] = tel
        continue
    elif secim == "2":
        sil = (input("Silmek istediginiz kisinin adini-soyadi :")).lower()
        for k in rehber.keys():
            if k == sil:
                rehber.pop(sil)
                print(sil.upper(), " adli kisi silindi...")
                break
            else:
                print("Bu ad-soyad bulunamadi..")
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
        print("Yanlis secim yaptiniz lutfen tekrar deneyin...\n")
        continue

dosya = open("telefonrehberi.txt", "w")
dosya.write("Ad-Soyad\tTelefon Numarasi\n")
for k, v in rehber.items():
    a = "{}\t{}\n".format(k.upper(), v.upper())
    dosya.write(a)
dosya.close()

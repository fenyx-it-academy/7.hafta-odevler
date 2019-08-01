##telefon rehberi uygulamasi
##Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
##Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim
##ya da tel bilgisi guncelleme, 
##rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli
##inputlarla programinizi sekillendirin.
##Olusturulan rehberi bir dosyaya kaydedin.
##Rehberi olustururken sozlukleri kullanin.

print("""<<<<<<<<< Telefon Rehberiniz >>>>>>>>>>>                        
Yapilabilecek Islemler:
1) Rehberinizi goruntulemek.
2) Rehberinize kisi eklemek.
3) Rehberinizden kisi silmek.
4) Kisi Ad&Soyad guncelleme.
5) Kisi telefon numarasi guncelleme.
6) Rehberden cikis.""")                                                             # kullaniciya program hakkinda bilgi verildi.
print("\n")

sozluk = {}                                                                         # bos bir sozluk olusturuldu.
while True:
    print("\n")
    secim = input("Lutfen bir islem seciniz:")                                      # kullanicidan yapilicak islem inputu alindi.
    if secim == "6":                                                                # 6 rakakmi girisi yapildiysa program kapatildi.
        print("Rehberiniz kapatiliyor...")
        quit()
    elif secim == "1":  
        if len(sozluk) == 0:                                                        # eyer sozluk bos ise len=0 rehberinin bos oldugu uyarisi yapildi.
            print("Suan listenizde kimse kayitli degil.")
            continue
        else:
            for anahtar,deger in sozluk.items():                                    # sozlukde herhangi bir oge var ise ekrana bastirildi.
                print("Ad & Soyad\t: {}, \tTelefon\t: {}".format(anahtar,deger))
    elif secim == "2":
        isim = input("Lutfen eklemek istediginiz kisinin adini ve soyadini giriniz:").lower()  # kisi eklemek icin bilgi inputu alindi ve butun harfler kucuk yazdirildi.
        if isim in sozluk.keys():                                                              # bilginin rehberde kayitli olup olmadigi kontrol edildi.
            print("Bu kisi rehberinizde zaten mevcut!!!")
            continue
        else:
            tel_no = input("Lutfen eklemek istediginiz kisini telefon numarasini giriniz:")    # kayitli degil ise tel no istenip sozluge isim=key, telefon=value olarak eklendi.
            print("Kisi rehberinize kaydedildi.")
            sozluk[isim] = tel_no 
    elif secim == "3":
        if len(sozluk) == 0:
            print("Suan listenizde kimse kayitli degil.")
            continue
        else:                                                       
            for anahtar,deger in sozluk.items():                                               # rehber listesi for dongusu ile ekrana bastirildi.
                print("Ad & Soyad\t: {}, \tTelefon\t: {}".format(anahtar,deger),"\n")
            sec = input("Lutfen silmek istediginiz kisinin Ad&Soyad bilgilerini giriniz:").lower()  # kullanicidan silmek istedigi kisinin bilgisi alindi.
            if sec not in sozluk:                                                                   # girilen isim rehberde yok ise uyari yapildi.
                print("Bu kisi rehberinizde kayitli degildir.")
            else:
                sozluk.pop(sec)                                                                     # isim rehberde var ise pop ile sozluk disina atildi.
                print(sec,", rehberinizden basariyla silindi.")        
    elif secim == "4":                                                                              
        if len(sozluk) == 0:
            print("Suan listenizde kimse kayitli degil.")
            continue
        else:
            for anahtar,deger in sozluk.items():                                            # rehber listesi kullaniciya gosterildi.
                print("Ad & Soyad\t: {}, \tTelefon\t: {}".format(anahtar,deger),"\n")
            guncel=input("Lutfen Ad&Soyad guncellemek istediginiz kisinin Ad&Soyad bilgilerini giriniz:").lower()
            if guncel not in sozluk:                                                        # girilen isim rehberde yok ise gereken uyari yapildi.    
                print("Bu kisi rehberinizde kayitli degildir. Guncelleme yapilamaz")
            else:                                                                           # mevcut ise yeni veri alindi ve eskisi silinip yenisi yazildi.
                yeni_adsoyad=input("Lutfen yeni Ad & Soyad bilgilerini giriniz:")
                updated=sozluk.pop(guncel)
                sozluk[yeni_adsoyad]=updated
                print("Guncellemeniz kayit edilmistir.")

    elif secim == "5":
        if len(sozluk) == 0:
            print("Suan listenizde kimse kayitli degil.")
            continue
        else:
            for anahtar,deger in sozluk.items():
                print("Ad & Soyad\t: {}, \tTelefon\t: {}".format(anahtar,deger),"\n")
            guncel=input("Lutfen telefon numarasi guncellemek istediginiz kisinin Ad&Soyad bilgilerini giriniz:").lower()
            if guncel not in sozluk:
                print("Bu kisi rehberinizde kayitli degildir. Guncelleme yapilamaz")
            else:
                yeni_numara=input("Lutfen yeni telefon numarasi bilgilerini giriniz:")
                sozluk.pop(guncel)
                sozluk[guncel]= yeni_numara
                print("Guncellemeniz kayit edilmistir.")
        
        
    else:
        print("Lutfen 'Yapilabilecek Islemler' listesinden bir secim yapiniz:")
        
    dosya=open("Rehber.txt","w")
    print("****TELEFON REHBERINIZ****".center(60), file=dosya)
    sira=1
    for anahtar,deger in sozluk.items():
        print(sira,")Ad & Soyad\t: {}, \tTelefon\t: {}".format(anahtar,deger),"\n", file=dosya,)
        sira+=1
    dosya.close()









        

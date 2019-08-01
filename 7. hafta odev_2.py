print("\nTELEFON REHBERI")                                                          # imza sablonumuzun ilk satirini yazdik
print("-" * 4, "ZAFER", "-" * 4, end="\n\n")                                        # imza sablonumuzun ikinci satirini yazdik
                                                                                    # kullaniciya karsilama metni ve menuyu sunduk
print("""Telefon rehberimize hosgeldiniz.                                        
Lutfen yapmak istediginiz islemi seciniz\n
    Rehbere kisi ekleme         1
    Rehberden kisi silme        2
    Rehberde degisiklik yapma   3
    Rehberi listeleme           4
    Rehberi dosyaya yazma       5 
    Cikis                       6
""")

rehber={}                                                                           # bos sozluk hazirladik
list_rehber=[]                                                                      # bos liste hazirladik

import time                                                                         # zaman fonksiyonunu aktive ettik

while True:                                                                         # muteaadit islem yapilacagi icin dongu olusturduk

    islem = input("\nLutfen yapmak istediginiz islemi seciniz : ")                  # kullanicidan yapacagi islemi talep ettik

    if islem == "1":                                                                # kullanicinin rehbere ekleme yapma secenegini kodladik
        adi=input("Adi : ")                                                         # kullanicidan verileri aldik
        soyadi=input("Soyadi : ")
        tel=input("Telefon numarasi : ")

        nam_sur = adi + " " + soyadi                                                # aldigimiz verileri hazirlayip rehber yazdik
        rehber[nam_sur] = tel
        print(rehber)

    elif islem == "2":                                                              # kullanicinin rehberde silme islemi yapma secenegini kodladik
        sil_ad = input("Lutfen silmek istediginiz kisinin adini giriniz : ")        # kullanicidan verileri aldik
        sil_soyad = input("Lutfen silmek istediginiz kisinin soyadini giriniz : ")
        sil=sil_ad + " " + sil_soyad                                                # aldigimiz verileri hazirlayip rehberden sildik
        rehber.pop(sil)
        print(rehber)

    elif islem == "3":                                                              # kullanicinin rehberde degisiklik yapma secenegini kodladik
        degisen_veri=input("Lutfen rehberinizdeki kisinin Ad - Soyad degisikligi icin 1`i, telefon numarasi degisikligi icin 2`yi secin : ")    # kullanicidan yapacagi islemi aldik

        if degisen_veri == "1":                                                             # kullanicinin rehberde ad soyad degisikligi secenegini kodladik
            eski_ad=input("Lutfen kisinin rehberde kayitli adini giriniz : ")               # kullanicidan eski ve yeni verileri aldik
            eski_soyad=input("Lutfen kisinin rehberde kayitli soyadini giriniz : ")
            yeni_ad=input("Lutfen kisinin yeni ad bilgisini giriniz : ")
            yeni_soyad = input("Lutfen kisinin yeni soyad bilgisini giriniz : ")

            rehber[yeni_ad + " " + yeni_soyad] = rehber[eski_ad + " " + eski_soyad]         # aldigimiz verilere gore rehberde degisiklik yaptik
            del rehber[eski_ad + " " + eski_soyad]
            print(rehber)

        elif degisen_veri == "2":                                                           # kullanicinin rehberde telefon no degisikligi secenegini kodladik
            eski_ad = input("Lutfen kisinin rehberde kayitli adini giriniz : ")             # kullanicidan eski ve yeni verileri aldik
            eski_soyad = input("Lutfen kisinin rehberde kayitli soyadini giriniz : ")
            yeni_tel = input("Lutfen kisinin yeni telefon numarasini giriniz : ")

            rehber[eski_ad + " " + eski_soyad] = yeni_tel                                   # aldigimiz verilere gore rehberde degisiklik yaptik
            print(rehber)

    elif islem == "4":                                                                      # rehberi listelemek icin gereken kodlamalari yaptik
        for k, v in rehber.items():
            veriler= k + "  :  " + v
            list_rehber.append(veriler)
        print(*list_rehber, sep="\n")

    elif islem == "5":                                                                      # rehberi dosyaya yazmak icin gereken kodlamalari yaptik
        with open("rehberim.txt", "a") as rehberim:                                         # rehberi yazacagimiz dosyayi actik
            for k, v in rehber.items():
                veriler = k + "  :  " + v
                list_rehber.append(veriler)
            print(*list_rehber, sep="\n", file=rehberim)
            print("Rehberiniz dosyaya yazdirildi.")

    elif islem == '6':                                                                      # programdan cikis icin gerekli kodlamalari yaptik
        print("\nProgramdan cikiyorsunuz...")
        time.sleep(2)
        print("\nProgramdan ciktiniz.")
        quit()

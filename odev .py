##telefon rehberi uygulamasi##
##hafta 7##


rehber = {"emrah":"065667788",
          "mustafa":"0635478632",
          "osman":"065276896542",
          "murat":"06387652829",
          "irfan":"06884833933"}
guncel = {}

while  True:
    print("""Yapabileceginiz islemler:

(1)kisi ekle
(2)kisi sil 
(3)rehberi guncelle
(4)rehberi listele

Cikmak icin lütfen q ya basiniz..
""")
    try:
        islem = input("Yapmak istediginiz islemi seciniz: ")
        if not islem:
            pass
        if islem =="1":
            isim = input("Eklenecek kisinin ismini giriniz: ")
            tel = input("Tel numarasini yaziniz: ")
            if tel.isdigit()!=True:
                print("Tel sadece sayılardan olusur")
                continue
            rehber[isim] = tel
            print(rehber)

        elif islem =="2":
            print(rehber)
            print("Lütfen listeden bir isim seciniz\n")
            isim = input("Silinecek kisinin ismini giriniz: ")
            if isim.lower() not in rehber:
                print("***BOYLE BIRISI YOK***\n\n")
                continue
            if isim.lower() in rehber:
                rehber.pop(isim.lower(),"malesef")
                print("REHBERİN SON HALİ:" ,rehber)

        elif islem == "3":
            print(rehber)
            isim = input("Guncellenecek isim giriniz: ")
            tel = input("tel numarasini giriniz:  ")
            guncel[isim] = tel
            rehber.update(guncel)
            print("guncellenmis rehber  :", rehber)

        elif islem =="4":
            for isim,tel in rehber.items():
                print("{} = {}".format(isim,tel))
        elif islem.lower() == "q":
            break
        else:
            print("***LUTFEN YAPABILECEGINIZ BIR ISLEM SECINIZ\n\n")
    except:
        print("Bilinmeyen bir hata olustu tekrar deneyiniz")

dosya=open("doosje.txt","w")
dosya.write(str(rehber))
dosya.close()

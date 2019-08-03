"""
telefon rehberi uygulamasi
Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme,
rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
Olusturulan rehberi bir dosyaya kaydedin.
Rehberi olustururken sozlukleri kullanin.
"""
b=[]
c=[]
rehber={}
with open("Telefon Rehberi.txt", "r+") as dosya:
    menu='''\t\t\t1-Kisi Ekleme
            2-Kisi Silme
            3-bilgi guncelleme
            4-Rehberi Listele
            5-Cikis
            '''
    for i in dosya:
        if ":" in i:
            b = i.split(":")
            if "\n" not in b:
                   c=b[1].split("\n")
                   rehber[b[0]] = c[0]
            else:
                    rehber[b[0]] = b[1]
    while True:
        print(menu)
        secim=input("Lutfen menuden yapmak istediginiz islemi seciniz.:")
        if secim=="1":
            isim=input("Eklemek istediginiz ismi giriniz")
            telefon=input("Eklemek istediginiz numarayi giriniz")
            if isim !='' or telefon!='' or isim !=' ' or telefon!=' ':
                if rehber.get(isim,"Yok")=="Yok":

                    rehber[isim] = telefon# Rehber sozlugune kisi ve numarasini ekledik.
                    print("Kisi ve Numara Rehbere eklendi.")
                else:
                    print("{} isimli kisi rehberde mevcut.".format(isim))
            else:
                print("isim yada telefon numarasi bos!!")
        elif secim=="2":
            try:
                sil=input("Silmek istediginiz kisinin ismini giriniz.")
                rehber.pop(sil)
                print("{} isimine ait numara rehberden silindi".format(sil))
            except KeyError:
                print("Kisi bulunamadi")
        elif secim=="3":
            tip=input("Ismi guncellemek icin 1 e , Noyu guncellemek icin 2 ye basiniz")
            if tip=="1":
                guncel_isim = input('Guncellemek istediginiz kisinin ismini giriniz.')
                yeni_isim= input("Yeni ismi giriniz:")
                number=rehber[guncel_isim]
                rehber.pop(guncel_isim)
                rehber[yeni_isim]=number
                print("{} isimli kisinin adi {} olarak guncellendi.".format(guncel_isim,yeni_isim))
            elif tip=="2":
                guncel_isim= input("numarasini guncellemek istediginiz kisinin ismini giriniz:")
                print("Bilgileri {} olan kisinin numarasini guncelleyeceksiniz".format(rehber[guncel_isim]))
                yeni_no=input("Yeni numarayi giriniz.")
                rehber[guncel_isim]=yeni_no
                print("Numara Guncellendi!!")
        elif secim=="4":
            for i,j in rehber.items():
                print(i,j)
        elif secim=="5":
            break
        else:
            print("Lutfen menudeki seceneklerden birini seciniz.")

with open ("Telefon Rehberi.txt", "w+") as file:
    for i,j in rehber.items():
        kisi=i+":"+j+"\n"
        file.write(kisi)

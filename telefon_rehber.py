dosya=open("telefon_rehberi.txt","r+",encoding="utf-8") #telefon rehberi klasoru olusturmustum.bunu yazilabilir okunabilir sekilde actim
satirlar=dosya.readlines()                              #her satir listeye donustu
telefon_rehberi={}

for i in satirlar:
    b=i.split(":")                                      #her satirda isim ve numara arasindaki : isaretinden ikiye ayirip iki indeksli liste olusturdum
    telefon_rehberi[b[0]]=b[1]                          # : dan onceki kisim KEY sonrasi VALUE oldu.her satiri rehber sozlugune ekledi

while True:
    print('''
    1   Yeni kayit/numara degistirme
    2   Telefon numarasi sorma
    3   Telefon Rehberine Git
    4   Kisi silme
    q   cikis''')
    islem = input("Yapmak istediginiz islemi girin:")                           #kullanici islem yapmak istemezse
    if islem == "q":
        break
    elif islem == '1':
        yeni_isim = input('isim:')
        if yeni_isim not in telefon_rehberi:                                    #kullanici yeni kayit yapacaksa
            yeni_numara = input("telefon numarasi:")
            telefon_rehberi[yeni_isim] = yeni_numara                            #sozluge isim:tel no eklendi
            print(yeni_isim + "     :   " + yeni_numara, "kisisi kaydedildi.")
        else:
            print("bu numara zaten kayitli.")                                   #var olan bir kisi secti
            devam = input("Devam etmek istiyor musunuz(e\h)")
            if devam == "e":                                                     #devam edip numara degistirecekse
                yeni_numara = input("telefon numarasi:")
                telefon_rehberi[yeni_isim] = yeni_numara
                print(yeni_isim + "     :   " + yeni_numara, "kisisi kaydedildi.")
            else:                                                               #var olan kisinin bilgilerini degistirmek istemezse
                print("Ana menuye donuluyor..")
    elif islem=="2":
        isim=input("isim giriniz:")
        numara=telefon_rehberi.get(isim,"kisi listesinde mevcut degil")         #herhangi birinin numarasini sorgulama
        print(isim+ "     :   " + numara)                                       #listede kisi yoksa uyari veriyor
    elif islem == "3":
        for isim in telefon_rehberi:
            print('{}   :   {}'.format(isim,telefon_rehberi[isim]).rjust(50))      #tum telefon rehberini gormek icin
    elif islem == "4":                                                              #kisi silmek
        silme = input("silmek istediginiz kisi ismi:")
        telefon_rehberi.pop(silme)
    else:
        print("Yanlis islem numarasi girdiniz")                                  #islem numaralari(1 2 3 4 q )disinda birsey yazilirsa anamenuye gecis




for isim in telefon_rehberi:
    yaz='{}:{}\n'.format(isim, telefon_rehberi[isim])                       #telefon rehberinin son halini dosyaya yazma
    dosya.write(yaz)
    dosya.close

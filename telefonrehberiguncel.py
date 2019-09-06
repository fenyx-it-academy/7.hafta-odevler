telefon="""Bu Bir Telofon Rehberi Guncelleme Programidir
Lutfen yapmak istediginiz islemi seciniz
Rehbere kisi eklemek icin :         1
Rehberden kisi silmek icin:         2
Rehberde degisiklik yapmak icin:    3
Islemden cikmak icin    :           q
basiniz!!!!\n"""
rehber={}
with open("information.txt", "r+") as telefonrehber:
    liste=telefonrehber.readlines()

for i in liste:
    boslist = []
    for k in i.split():
        boslist.insert(0,k)
    degerrehber={boslist[1]:boslist[0]}
    rehber.update(degerrehber)
while True:
    print(rehber)
    secim=input(telefon)
    if secim=="q":
        break
    elif secim=="1":
        isim=input("lutfen ismi giriniz")
        numara=input("lutfen numara giriniz")
        rehber.setdefault(isim,numara)
        continue
    elif secim=="2":
        try:
            silme=input("Silmek istediginiz kisiyi seciniz:")
            rehber.pop(silme)
        except KeyError:
            print("silmek istediginiz kisi listede yoktur")
            continue
        continue
    elif secim=="3":
        degisim=input("degistirmek istediginiz numarayi yada kisiyi giriniz")
        deger1=list(rehber.keys())        #isimler listeye donustu
        deger2=list(rehber.values())       #numaralar listeye donustu
        if degisim in deger1:              #bu kod blogunu kisi ismi yada numarayi guncellemek isteyebilir bu yuzden yazdim
            while True:
                yenideger=input("lutfen yeni ismi giriniz")  #yeni ismi gir
                if yenideger in deger1:
                    print("bu isim zaten rehberinizde var")
                    continue
                else:
                    break
            sira=deger1.index(degisim)    #aradigimiz isim listenin kacinci sirasinda
            deger1.pop(sira)              #listedeki o ismi sil
            sira1=deger2.pop(sira)        #isme denk gelen numarayi sil ama hafizada tut
            rehber.pop(degisim)           #sozlukte o blogu sil
            deger1.insert(sira,yenideger)   #yeni ismi isim listesinin ayni sirasina ekle
            deger2.insert(sira,sira1)       #ismin eski numarasini ayni siraya numara listesine ekle
            rehber3={deger1[sira]:deger2[sira]}  #listeyi sozluge cevir
            rehber.update(rehber3)              #yeni degeri sozluge ekle
            continue
        if degisim in deger2:
            while True:
                yenideger=input("lutfen yeni numara giriniz")  #yeni ismi gir
                if yenideger in deger2:
                    print("bu numara zaten rehberinizde var")
                    continue
                else:
                    break
            sira=deger2.index(degisim)
            servis=deger2.pop(sira)
            sira1=deger1.pop(sira)
            deger1.insert(sira,sira1)
            deger2.insert(sira,yenideger)
            rehber3={deger1[sira]:deger2[sira]}
            rehber.update(rehber3)
            continue
        else:
            print("Degistirmek istediginiz deger rehberde yoktur")
print(rehber)
telefonrehber = open("information.txt", "a")
for isim, numara in rehber.items():
    telefonrehber.write(isim+"\t")
    telefonrehber.write(numara+"\n")
quit()

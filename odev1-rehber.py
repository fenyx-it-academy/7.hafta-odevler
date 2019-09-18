import time
rehber={}
onbellek=[]
with open('rehber.txt','a+',encoding='utf-8') as a:
    a.close()
#sozlugumuzu kaydedecegimiz dosyayi olusturduk
#kaydedecegimiz dosyayi acip kapattik burada sadece
with open("rehber.txt", "r", encoding="utf-8") as f:
    f.seek(0)
    for i in f:
        for i in f:
            if i == "":
                continue
            else:
                onbellek = i.split("=")
                rehber[onbellek[0]] = onbellek[1]
#burada dosyayi okuma modunda actik ve onbellek adli
# rehberdeki numara ve isimleri for dongsu ile
#onbellek adli listemize aldik ve ordan rehber adli sozlugumuze gecirdik
#boylelikle sistem her calistiginda dosyadan bilgileri cekiyor
while True:
    print('Lutfen yapmak isdeginiz islemi seciniz:')
    islem = input("rehbere yeni kisi eklemek icin 1'e\n\
    rehberdeki kisiyi silmek icin 2'ye\n\
    isim bilgisi guncellmek icin 3'e\n\
    numara bilgisi guncellemek icin 4'e\n\
    rehberi goruntulemek icin 5'e basiniz\n\
    cikmak icin lutfen q'ya basiniz :")
    if islem=='q':
        print('Programdan cikiliyor!')
        time.sleep(3)
        break
    elif islem=='1' :
        isim=input('Lutfen eklemek istediginiz ismi giriniz :')
        numara=input('Lutfen eklemek istediginiz numarayi giriniz :')
        if isim=='' or numara=='' :
            print('isim veya numara bos birakilamaz !')
            time.sleep(3)
            continue
# eger bos degilse bu sefer for dongusu yardimiyla rehberde ayni
# isim olup olmadigi kontrol ediyoruz ve bunun olmasi durumunda
#kullaniciya hata mesajimizi veriyoruz
        else :
            for i in rehber :
                if i==isim:
                    print('Ayni isimde birden fazla kayit olamaz!')
                    time.sleep(3)
                    continue
# for dongusu ile baktiktan sonra eger rehberde yoksa
# yeni kisi rehbere ekleniyor
            else:
                print('Kisi ekleniyor')
                rehber[isim]=numara
                print()
                time.sleep(2)
# eger kullanici bir kisiyi silmek isterse kullanicidan
# input alarak kisiyi siliyoruz eger kisi yoksa
# bunu bi hata mesaji vererek donguyu tekrarliyoruz
    elif islem=='2':
        for x, y in rehber.items():
            print(f'{x}={y}')
        kisisilme=input('Lutfen silmek istediginiz kisinin ismini giriniz!')
        if kisisilme in rehber.keys():
            print('Kisi siliniyor!')
            del rehber[kisisilme]
            time.sleep(2)
            continue
        else:
            print('Lutfen rehberde bulunan bir isim giriniz!')
            time.sleep(2)
            continue
# kullanici eger kisi ismi guncellemek isterse for dongusu ile rehberde
# kullanicinin silmek istedigi ismin olup olmadigi kontrol ettik
# eger yoksa diger for dongusune giriyor ve pop yardimiyla eski ismi silip
# yeni isimi rehbere ekliyoruz
    elif islem=='3':
        for x, y in rehber.items():
            print(f'{x}={y}')
        guncelleme=input('Lutfen guncellemek istediginiz kisi ismini girin :')
        for i in rehber.keys() :
            if i != guncelleme:
                print('Lutfen gecerli bir isim giriniz!')
                time.sleep(2)
                continue
        for i in rehber.keys() :
            if guncelleme==i :
                degisim=input('Lutfen yeni kisi ismini yaziniz:')
                rehber[degisim]=rehber.pop(guncelleme)
                print('Kisi guncelleniyor!')
                time.sleep(2)
# eger kullanici numara guncellemek isterse for ile rehberde kisinin kayitli
# olduguna bakiyoruz ve eger varsa yeni numaramizi giriyoruz
    elif islem=='4':
        guncelleme = input('Lutfen numarasini guncellemek istediginiz kisi ismini girin :')
        for i in rehber:
            if i == guncelleme:
                degisim = input('Lutfen yeni numarayi yaziniz:')
                rehber[i] = degisim
        if guncelleme not in rehber.keys() :
            print('Lutfen rehberde kayitli bir ismi giriniz!')
            time.sleep(2)
            continue
# en son olarak eger rehberi goruntulemek isterse bunu kullaniciya gosterebiliyoruz
    elif islem=='5':
        print('Rehberiniz')
        for x,y in rehber.items() :
            print(f'{x}={y}')
        time.sleep(5)
# burada da dosyamiza yazmasi icin programda yaptigimiz degisiklikleri
#dosyaya yazdiriyoruz
with open("rehber.txt","a+",encoding="utf-8") as w:
    for i,j in rehber.items():
        w.write(i)
        w.write("=")
        w.write(j)
        w.write("\n")
rehber = {}
import time
dosya=open('Rehber.txt','a+')
while True :
#bos bi kume actik ve ileride kullanicinin yaptigi islemlerden
#sonra erkanda printleri gorebilmesi icin impor time modulune girdik
    print('Lutfen yapmak isdeginiz islemi seciniz:')

    islem=input("rehbere yeni kisi eklemek icin 1'e\n\
rehberdeki kisiyi silmek icin 2'ye\n\
isim bilgisi guncellmek icin 3'e\n\
numara bilgisi guncellemek icin 4'e\n\
rehberi goruntulemek icin 5'e basiniz\n\
cikmak icin lutfen q'ya basiniz :")
#kullanicidan yapmak istedigi islemi belirlemesi icin
#input aldik
    if islem=='q':
        print('Programdan cikiliyor!')
        time.sleep(3)
        break
#kullanici eger yeni bir kayit girmek isterse bunun
#once bos karakter olup olmadigini kontrol ediyoruz

    elif islem=='1' :
        isim=input('Lutfen eklemek istediginiz ismi giriniz :')
        numara=input('Lutfen eklemek istediginiz numarayi giriniz :')
        if isim=='' or numara=='' :
            print('isim veya numara bos birakilamaz !')
            time.sleep(3)
            continue
#eger bos degilse bu sefer for dongusu yardimiyla rehberde ayni
#isim olup olmadigi kontrol ediyoruz ve bunun olmasi durumunda
#kullaniciya hata mesajimizi veriyoruz
        else :
            for i in rehber :
                if i==isim:
                    print('Ayni isimde birden fazla kayit olamaz!')
                    time.sleep(3)
                    continue
#for dongusu ile baktiktan sonra eger rehberde yoksa
#yeni kisi rehbere ekleniyor
            else:
                print('Kisi ekleniyor')
                rehber[isim]=numara
                time.sleep(2)
#eger kullanici bir kisiyi silmek isterse kullanicidan
#input alarak kisiyi siliyoruz eger kisi yoksa
#bunu bi hata mesaji vererek donguyu tekrarliyoruz

    elif islem=='2':
        for x, y in rehber.items():
            print('{}={}'.format(x, y), file=dosya, flush=True)
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
#kullanici eger kisi ismi guncellemek isterse for dongusu ile rehberde
#kullanicinin silmek istedigi ismin olup olmadigi kontrol ettik
#eger yoksa diger for dongusune giriyor ve pop yardimiyla eski ismi silip
#yeni isimi rehbere ekliyoruz
    elif islem=='3':
        for x, y in rehber.items():
            print('{}={}'.format(x, y), file=dosya, flush=True)
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

#eger kullanici numara guncellemek isterse for ile rehberde kisinin kayitli
#olduguna bakiyoruz ve eger varsa yeni numaramizi giriyoruz
    elif islem=='4':
        for x, y in rehber.items():
            print('{}={}'.format(x, y), file=dosya, flush=True)
        guncelleme = input('Lutfen numarasini guncellemek istediginiz kisi ismini girin :')
        for i in rehber:
            if i == guncelleme:
                degisim = input('Lutfen yeni numarayi yaziniz:')
                rehber[i] = degisim
        if guncelleme not in rehber.keys() :
            print('Lutfen rehberde kayitli bir ismi giriniz!')
            time.sleep(2)
            continue

    elif islem=='5':
        print(dosya.read())
        print('Rehberiniz')
        for x,y in rehber.items() :
            print('{}={}'.format(x,y))
            time.sleep(5)

#en son olarak eger rehberi goruntulemek isterse bunu kullaniciya gosterebiliyoruz
#ama eger dosyadan okumak isterse o olmuyor read komutu neden calismadigini anlamadim
    for x, y in rehber.items():
        print('{}={}'.format(x, y),file=dosya,flush=True)
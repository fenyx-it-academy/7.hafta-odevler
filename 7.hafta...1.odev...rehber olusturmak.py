print('b.')
'''
###...telefon rehberi uygulamasi...###
>>>..Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
A...> Program acildiginda kullaniciya,
 1-rehbere kisi ekleme, 
 2-kisi silme, 
 3-kisi isim ya da tel bilgisi guncelleme, 
 4-rehberi listeleme seceneklerini sunun. 
B...> Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
C...> Olusturulan rehberi bir dosyaya kaydedin.
not: Rehberi olustururken sozlukleri kullanin.
'''
giris='''
1-reh kisi ekle
2-kisi silme
3-bilgi guncelleme
4-rehberi goster
5-dosya kaydet
>>>>...cikis icin bir tusa basiniz
'''
with open("rehber1.txt", "r", encoding='utf-8') as f:
    veri=f.read()
rehber={}                                   # bos bir sozluk olusturduk
for i in veri.split('\n'):
    kisi=i.split(':')
    rehber[kisi[0]]=kisi[1]                 #dosyamizda mevcut kayitli olan kisileri rehberimize ekledik
while True:
    print(giris)
    cvp=input('tercih yapiniz....>>>')
    if cvp =='1':                           # kisi ekleme
        isim=input('isimi giriniz....:')
        tel=input('tel giriniz...:')
        rehber[isim]=tel                    #sözlük[anahtar] = değer

    elif cvp == '2':                        # kisi silme
        isim=input('silmek istediginiz ismi giriniz....:')
        if isim in rehber:
            rehber.pop(isim)
        else:
            print('girmis oldugunuz isim rehberde yok')
            continue
    elif cvp== '3':                         #bilgi guncelleme
        isim = input('guncellemek istediginiz kisinin ismini giriniz')
        if isim in rehber:
            print("{} nin telefon numarası: {}".format(isim, rehber[isim]))
            yeni_tel=input('yeni tel no giriniz...:')
            rehber[isim]=yeni_tel
        else:
            print("Aradığınız kişi rehberde yok!")
            break
    elif cvp == '4':                        #rehberi goster
        for isim,tel in rehber.items():
            print(isim,':',tel)

    elif cvp == '5':                        # dosya kayit
        with open('rehber1.txt', 'w') as f:
            for isim,tel in rehber.items():
                print(f'{isim} : {tel}',file=f)

    else:
        print('cikiliyor....bye')
        quit()

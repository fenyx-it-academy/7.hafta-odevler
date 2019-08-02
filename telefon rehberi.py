# coding=utf-8

menu=[' -----------------------------------------------------',
'|                                                     |',
'|      Telefon rehberi uygulamasına hos geldiniz.     |',
'|                                                     |',
'|      Telefon rehberine kişi eklemek için 1 e,       |',
'|                                                     |',
'|      Rehberden kişi silmek için 2 ye,               |',
'|                                                     |',
'|      Bilgi güncelleme için 3 e,                     |',
'|                                                     |',
'|      Tüm rehberi görmek için 4 e basınız.           |',
'|                                                     |',
'|      Rehberden çıkmak için ise q ya basınız.        |',
'|                                                     |',
' -----------------------------------------------------']

for i in menu:
    print ('\t'.expandtabs(30), i) #acılıs metnini ekranın oratsına yazdırma

tel_rehber={}

while True:
    with open('Telefon rehberi.txt', 'w') as rehber_kayit: #yazma modunda txt dosyası acılıyor
        for key, value in tel_rehber.items(): # sozlukdeki herbir anahtar-deger cifti
            rehber_kayit.write('{} = {}'.format(key, value)) # acılan dosyaya yazdırılıyor

    secim = input('\nLütfen bir seçim yapınız =\n') #kullanıcıdan yapıacak islem secimi

    if secim=='m': # acılıs metnini tekrar yazdırma
        for i in menu:
            print ('\t'.expandtabs(25), i)

    elif secim=='1': #rehber isim ekleme girisi
        isim_ekle=input('Rehbere eklenecek isimi yazınız = \n').capitalize() #kullanıcıdan isim girisi ve isimlerin bas harfini buyutme
        tel_rehber[isim_ekle]=input('Telefon numarasını yazınız = \n') #eklene isim icin kullanıcıdan tel no girisi ve sozluge atama yapma

    elif secim=='2': #kayıt silme girisi
        isim_sil=input('Silmek istediğiniz kişinin ismini yazınız = \n')
        tel_rehber.pop(isim_sil) #sozlukten kısı silme

    elif secim=='3': #tel no guncelleme girisi
        guncel_isim=input('Telefon numarasını güncellemek istediğiniz kişinin ismini yazınız.\n') #nosu guncellenecek kisinin isiminin secimi
        tel_rehber[guncel_isim]=input('Yeni telefon numarasını giriniz.\n') #secilen kısını tel nosunu yeniden atama

    elif secim=='4': #sozlugun tamamının ekranan yazdırılması
        with open('Telefon rehberi.txt', 'r') as rehber_kayit: #rehberin kayıtlı oldugu dosyanın okuma modunda acılması
            for i in rehber_kayit: #dosyadakı herbir satır icin dongu
                print(i)

    elif secim=='q':
        quit()

    else:
        print ('''Lütfen size belirtilen seçeneklerden birini giriniz.\n
Not: Ana menüye dönmek için 'm'ye basınız.\n''')








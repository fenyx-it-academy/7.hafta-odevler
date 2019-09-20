# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:30:07 2019

@author: HP
"""

#telefon rehberi uygulamasi 
# Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
#Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme,
#rehberi listeleme seceneklerini sunun.Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
#Olusturulan rehberi bir dosyaya kaydedin.Rehberi olustururken sozlukleri kullanin.

print("Telefon Rehberi Uygulamasina Hosgeldiniz...")
telefon_rehberi = {"ahmet oz" : "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz" : "0533 533 33 33",
                   "eda ala"  : "0212 212 12 12"}

while True :
    with open('Telefon rehberi.txt', 'w') as Telkayit: 
        for key, value in telefon_rehberi.items(): 
            Telkayit.write('{} = {}'.format(key, value)) 
            
    kisi=input("""Rehbere kisi eklemel icin 1 e
                     Rehberden kisi silmek icin 2 ye
                     Rehberde kisinin ismini guncellemek icin 3 e
                     Rehberde kisinin telefon numarasini guncellemek icin 4 e
                     Rehberi gostermek icin 5 e
                     Rehberden cikmak icin q' ya basiniz ;""")
    if kisi=="1":
        isim=input('Ad Soyad giriniz;')
        tel_no=input('Telefon numarasini giriniz ;')
        mesaj = "{} kisisi rehbere eklendi!"
        telefon_rehberi[isim] = tel_no
        print(mesaj.format(isim))
    elif kisi=="2":
        sil_isim=input('Silinmesini istediginiz kisinin adini giriniz')
        telefon_rehberi.pop(sil_isim)
        print('{} adlı kişi rehberden silindi'.format(sil_isim))
    elif kisi=='3':
        eski_isim=input('Guncellenmesini istediginiz kisinin adini giriniz')
        x=telefon_rehberi.pop(eski_isim)
        yeni_isim=input('Guncellenecek yeni ismi giriniz')        
        telefon_rehberi[yeni_isim] = x
        print('{} adlı kişi rehberde guncellendi'.format(yeni_isim))
    elif kisi=='4':
        guncel_kisi=input('Numarasi guncellenecek kisinin ismini giriniz ;')
        yeni_numara=input('Yeni numarayi giriniz ;')
        telefon_rehberi[guncel_kisi] = yeni_numara        
    elif kisi=='5':
        with open('Telefon rehberi.txt', 'r') as Telkayit: 
            for key in Telkayit:
                print(key,'\n')
                
        #for key,value in telefon_rehberi.items() :
         #   print('Kisi=',f'{key}',' ; Tel No=', f'{value}')
    elif kisi=='q':
        print('Cikiliyor...')
        break




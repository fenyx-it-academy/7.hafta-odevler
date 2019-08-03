print('*'*30+'\n\n'+'Telefon Rehberi'.rjust(22)+'\n\n'+'1.Isim Ara\n'+'2.Yeni Isim Ekle\n'+'3.Isim ve Numara Guncelle\n'
      +'4.Isim Sil\n'+'5.Rehber Listesi\n'+'Cikis icin "q" ya basin!\n\n'+'*'*30+'\n')

try:
    islem = ''
    isim = ''
    numara = ''
    # isim ve numaralari kaydedecegimiz sozlugumuzu olusturduk
    telefonRehberi = {
        isim: numara,
    }
    while islem != 'q':
        # hem okunabilen hem yazilabilen txt dosyasi actik
        rehberListesi = open(r"rehberListesi.txt", "r+")
        islem = input('Bir Islem Girin:')
        if islem == '1':
            try:
                isim = input("Numarasini ogrenmek istediginiz isim:")
                print('{} : {}'.format(isim, telefonRehberi[isim]))
            except:
                print('Aradiginiz kisi rehberde yok.')
                continue
        elif islem == '2':
            isim = input("Isim:")
            numara = input('Telefon Numarasi:')
            # kullanicinin eklemek istedigi isim ve numarayi sozluge kaydettik
            telefonRehberi.update({isim: numara})
            # actigimiz dosyaya sozlukteki gincel isim ve numaralari yazdiriyoruz
            for key, value in telefonRehberi.items():
                if key and value is not None:
                    rehberListesi.write(key + ': ' + value + '\n')
            rehberListesi.close()
            print('Isim ve numara basarili bir sekilde eklendi.')
        elif islem == '3':
            try:
                isim = input("Guncellemek istediginiz isim:")
                yeniIsim = input("Yeni Isim:")
                # sozlukten eski ismi silip yeni ismi atiyoruz
                telefonRehberi[yeniIsim] = telefonRehberi.pop(isim)

                yeniNumara = input('Yeni telefon numarasi:')
                # yeni ismimizin degerini yani numarayi yazdiriyoruz
                telefonRehberi[yeniIsim] = yeniNumara
                print('Isim ve numara basarili bir sekilde guncellendi.')

                for key, value in telefonRehberi.items():
                    if key and value is not None:
                        rehberListesi.write(key + ': ' + value + '\n')
                rehberListesi.close()
            except:
                print('Yazdiginiz isim rehberde yok.')
                continue
        elif islem == '4':
            try:
                isim = input("Silinecek isim:")
                # sozlukten anahtar ismi sildik,degeri de silindi
                telefonRehberi.pop(isim)
                for key, value in telefonRehberi.items():
                    if key and value is not None:
                        rehberListesi.write(key + ': ' + value + '\n')
                rehberListesi.close()

                print('Isim ve numara basarili bir sekilde silindi.')
            except:
                print('Silmeye calistiginiz isim rehberde yok.')
                continue
        elif islem == '5':
            # rehberdeki isim sayisini bulmak icin sayac olustr.
            a = 0
            # sozlugun key ve value larini yazdirdik
            for key, value in telefonRehberi.items():
                if key and value is not None:
                    a += 1
                    rehberListesi.write(key + ': ' + value + '\n')
                print(key, value)
            rehberListesi.close()
            print('\nRehberinizde {} isim bulunmaktadir.'.format(a))
        else:
            print('Lutfen gecerli bir islem girin!')
            continue
except:
    print('Hatali islem!')






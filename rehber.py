liste={}

kayit=""
while True:
    #---------------SECME INPUTU-----------------------------
    print("\n________________REHBERIM MENU_____________________\n")
    secim=input("""
Yeni Kayit : K
Kisiler    : R                                         CIKIS=Q
---------> :""").upper()

    if secim=='Q':
        print('Cikiliyor.....')
        break
    elif secim=='K':

        yeni_kisi = input('         Adi ve Soyadi :' ).upper()

        while True:

            telefon=input('         Telefon No    :')

            if len(telefon)!=10 :
                print('lutfen 10 haneli telefonunuzu giriniz')
                continue
            else:
                tel = f'+31 {telefon[0 :3]} {telefon[3 :6]} {telefon[6 :8]} {telefon[8 :10]}'
                break

        #------------SOZLUGE EKLEME-----------------------

        liste[yeni_kisi]=tel
        print('\nBasariyla kaydedildi...\n')

        #------------DOSYAYA YAZMA----------------------------------
        with open ( "rehber.txt" , "w"  ) as rehber :

            for oku,yaz in liste.items():

                kayit=f'{oku} : {yaz} ''\n'

                rehber.write(kayit)

    #----------------REHBERE GIRIS INPUTU----------------------------
    elif secim== 'R' :

        while True:
            if liste == {} :
                print ( 'Rehberinizde kayit yok.' )
                break
            else :
            #---------REHBERI GOSTERME-------------------
                for anahtar, deger in liste.items () :

                    print ( ">>>{} : {}".format ( anahtar , deger ) )

    #----------REHBER ICINDEKI SECIMLER------------------------

            duzen = input ( """
>>>>>>>>>>>>>>>>>>>>>

                    Kayit Sil      : S
                    Kayit Yenile   : Y
                    Tumunu sil     : T
                    Ana menu       : X
              >>>>>>>>>>>>>>>>>>>> :""" ).upper()
        #------------ANA MENUYE DONUS----------------------
            if duzen=='X':
                print('Ana Menuye donuluyor... ')
                break

        #---------REHBERDEN ISIM SILME----------------------
            elif duzen=='S':
                for anahtar ,deger in liste.items () :
                    print ( "{}  : {}".format ( anahtar , deger ) )

                while True:

                    sil=input('\n''silmek istediginiz ismi giriniz(cikis ENTER) :').upper()
                    if sil=='':

                        break
                    elif sil in liste:
                        liste.pop(sil)   #POP() KOMUTU ILE SILINDI
                        with open ( "rehber.txt" , "w" ) as rehber :

                            for oku , yaz in liste.items () :
                                kayit = f'{oku} : {yaz} ''\n'

                                rehber.write ( kayit )
                        print ( 'Kayit silindi simdi Ana menuye yonlendiriliyorsunuz....' '\n')

                        break
                    else:
                        print('kayit bulunamadi')
                        continue

            #----------REHBERDE ISIM NO GUNCELLEME-----------------

            elif duzen=='Y'  :
                for anahtar,deger in liste.items () :
                    print ( "{}  : {}".format ( anahtar , deger ) )


                while True :
                    guncelle = input ( '\n''lutfen guncellemek istediginiz ismi giriniz(cikis ENTER)' ).upper()
                    if guncelle=='':
                        break

                    elif guncelle not in liste:
                        print('kayit bulunamadi' )
                        continue
                    else:
                        liste.pop ( guncelle )
                        break
                yeni_giris = input ('\n''Yeni ismi Giriniz:' ).upper()
                while True:

                    yeni_giris2 = input ( 'Yeni Tel No:' )

                    if len ( yeni_giris2 ) != 10 :
                        print ( 'lutfen 10 haneli telefonunuzu giriniz' )
                        continue
                    else :
                        tel = f'+31 {yeni_giris2[0 :3]} {yeni_giris2[3 :6]} {yeni_giris2[6 :8]} {yeni_giris2[8 :10]}'

                        break
                #-------------UPDATE KOMUTU ILE GUNCENLENDI-----------
                up_dte={yeni_giris:yeni_giris2}
                liste.update(up_dte)
                with open ( "rehber.txt" , "w" ) as rehber :

                    for oku , yaz in liste.items () :
                        kayit = f'{oku} : {yaz} ''\n'
                        print ( kayit )
                        rehber.write ( kayit )

                print('isleminiz basariyla gerceklestirildi.')

            # ----------REHBERIN HEPSINI SILME-----------------
            elif duzen=='T'  :
                liste.clear()   #CLEAR() KOMUTU ILE TEMIZLENDI
                print('tum liste temizlendi')
                with open ( "rehber.txt" , "w" ) as rehber :
                    rehber.write('')

            else:
                print('Lutfen dogru tusa bastiginizdan emin olun')
                continue

            break
    else:
        print('Yanlis bir tusa bastiniz')

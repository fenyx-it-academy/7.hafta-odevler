print("""
            Tel Rehberi Programi
            
        Yapmak İstediginiz İslemi Seciniz:

            1- Rehbere kisi ekleme,
            2- Rehberden kisi silme,
            3- Rehberde kisi ismi guncelleme,
            4- Rehberde tel no guncelleme,
            5- Rehberi goruntuleme

            Cikmak icin: q ya da Q


        """)
rehber={"isim":"tel no"}                       #rehber olarak sozluk kullanildi.
print("Rehber: ",rehber)

while True:
    secim=input("Lutfen seciminizi belirtiniz: ")
    if secim=="q" or secim=="Q":
        print("Sistemden Cikiliyor...")
        quit()
    elif secim=="1":
        isim=input("Rehbere eklemek istediginiz ismi giriniz: ").upper() #Rehbere eklenen tum isimler buyuk harfle kayit ediliyor.
        while True:            
            tel=input("Bu isme ait tel no'yu giriniz:06- ")
            if len(tel)!=10:
                print("10 haneli tel nonuzu giriniz...")
                continue
            else:
                break
        rehber[isim]=tel
        print("Yeni kisi Rehbere eklendi.")
        
        with open ( "Rehber.txt" , "w" ) as dosya :         #Rehber isimli dosyaya kayit ediliyor.
            for key,value in rehber.items():
                kayit=f'{key} : {value} ''\n'
                print(kayit)
                dosya.write(kayit)
                
                
        continue
    elif secim=="2":
        isim2=input("Rehberden silmek istediginiz ismi giriniz: ").upper()
        while True:           
            if isim2=="":
                print("Lutfen gecerli bir isim giriniz.")
                break
            elif not isim2 in rehber:
                print("Bu isim zaten rehberde kayitli degil.")
                break
            else:
                rehber.pop(isim2)
                print(rehber)
                with open ( "Rehber.txt" , "w" ) as dosya :
                    for key,value in rehber.items():
                        kayit=f'{key} : {value} ''\n'
                        print(kayit)
                        dosya.write(kayit)
                break

    elif secim=="3":
        isim3=input("Ismini guncellemek istediginiz ismi yazin: ").upper()
        if isim3=="":
            print("Lutfen gecerli bir isim giriniz.")
        elif not isim3 in rehber:
            print("Bu isim zaten rehberde kayitli degil.")
            break    
        else:
            guncel_isim3=input("Yeni ismi giriniz: ").upper()
            rehber[isim3]=guncel_isim3
            print(rehber)
            with open ( "Rehber.txt" , "w" ) as dosya :
                    for key,value in rehber.items():
                        kayit=f'{key} : {value} ''\n'
                        print(kayit)
                        dosya.write(kayit)
        continue
    elif secim=="4":
        guncel_isim=input("Telefonunu guncellemek istediginiz ismi yazin: ").upper() #guncelleme yapmak icin var olan isimlerden secim yapilabilir
        if guncel_isim=="":
            print("Lutfen gecerli bir isim giriniz.")
        elif not guncel_isim in rehber:
            print("Bu isim zaten rehberde kayitli degil.")
            break
        else:
            guncel_tel=input("Guncel numarayi giriniz: ")
            rehber[guncel_isim]=guncel_tel
            print(rehber)
            with open ( "Rehber.txt" , "w" ) as dosya :
                    for key,value in rehber.items():
                        kayit=f'{key} : {value} ''\n'
                        print(kayit)
                        dosya.write(kayit)
        continue
    elif secim=="5":
        if rehber=={}:
            print("Rehberde kayitli kimse yok...")
            break
        else:           
            for key,value in rehber.items():
                print(key,value)

    else:
        print("Hatali giris yaptiniz...","Tekrar deneyin...")
        continue


print('''
                        TELEFON REHBERI UYGULAMASI

Lutfen yapmak istediginiz islemi verilen yonergeden seciniz.

Rehberi Listeleme--------------------------------------> 0
Rehbere Kisi Ekleme------------------------------------> 1
Rehberden Kisi Silme-----------------------------------> 2
Kisi Isim Guncelleme-----------------------------------> 3
Kisi Tel No Guncelleme---------------------------------> 4
Cikis--------------------------------------------------> 5
''')

rehber={}

while True:
    giris=int(input("\nSectiginiz islem numarasini giriniz : "))
    
    if giris==5:
        break

    elif giris==0:
        print(rehber)

    elif giris==1:
        yeni_kisi=input("Eklenecek kisinin adi: ")
        yeni_no=input("Eklenecek kisinin numarasi: ")
        print("{} adli kisinin {} nolu telefonu rehbere eklenmistir".format(yeni_kisi,yeni_no))
        rehber[yeni_kisi]=yeni_no

    elif giris==2:
        silinen_kisi=input("Silinecek kisinin adi :")
        rehber.pop(silinen_kisi,"Boyle biri rehberinizde bulunmamaktadir.")
        print("{} adli kisi rehberinizden silinmistir.".format(silinen_kisi))

    elif giris==3:
        eski_kisi=input("Guncellemek istediginiz kisinin sistemdeki adi: ")
        guncel_kisi=input("Kisinin guncel adi: ")

        if eski_kisi in rehber:
            
            rehber[guncel_kisi]=rehber[eski_kisi]
            del rehber[eski_kisi]
            print("{} adli kisinin ismi {} olarak degistirilmistir.".format(eski_kisi,guncel_kisi))

        else:
            print("Boyle biri rehberinizde yer almamaktadir")

    elif giris==4:
        kisi=input("Numarasini guncellemek istediginiz kisinin adi: ")
        guncel_no=input("Yeni numarayi giriniz: ")

        if kisi in rehber:
            rehber[kisi]=guncel_no
            print("{} adli kisinin yeni numarasi {}".format(kisi,guncel_no))

        else:
            print("Boyle biri rehberinizde yer almamaktadir")

dosya=open("rehber.txt","w+")
dosya.write(str(rehber))
dosya.close()
            
            
            
            
        
        
        
        

        
        
        

                

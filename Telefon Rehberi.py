print("""
      =============================================="
      |                                            |
      |                                            |
      |             TELEFON REHBERI                |
      |               HOSGELDINIZ                  |
      |                                            |
      ==============================================\n\n""")

veritabani = {}         #Numara ve ismi atacagimiz sozluk
guncellenen = {}        # 3.secenegi yazarken olusturmak zorunda kaldim.
                        # Guncellenen yeni isim ve noyu once buraya sonra ana sozluge atcaz

while True:

    islem = input("""Lutfen Yapmak IStediginiz Islemi Seciniz !
    
    1. Kisi Ekleme
    2. Kisi Silme
    3. Kisi Yada Numara Guncelleme
    4. Rehberi Listeleme
    
    Secenek : """.upper())

    while True:
        if islem=="1":
            isim = input("Eklemek Istediginiz Kisinin Adini Giriniz : ")
            numara = input("Eklemek Istediginiz Kisinin Numarasini Giriniz : ")
            veritabani[isim] = numara           #bu islem girilen isim ve numarayi sozluge atiyor
            print(veritabani)
            islem2 = input("""
            Kisi Eklemeye Devam Etmek Icin ENTER' a Basiniz, Bir Ust Menuye Donmek Icin baska bir tusa  Basiniz! : """.upper())
            if islem2=="":
                continue
            else:
                break

        if islem=="2":
            secim= input("Lutfen Bilgilerini Silmek Istediginiz Kisinin adini yaziniz ! :")
            veritabani.pop(secim)       #veritabanindan girilen isme ait bilgileri siler
            print(veritabani)
            islem2 = input("""Kisi Silmeye Devam Etmek Icin ENTER' a Basiniz, Bir Ust Menuye Donmek Icin baska bir tusa  Basiniz! : """.upper())
            if islem2 == "":
                continue
            else:
                break


        if islem=="3":
            secim3 = input("Lutfen Bilgilerini Guncellemek Istediginiz Kisinin Ismini Giriniz : ")
            print("Numara : ",veritabani[secim3])
            veritabani.pop(secim3)      # Guncellenmesini istedigimiz kisi bilgilerini kisiyi belirttikten sonra  siliyoruz
            ad = input("Yeni Ismi Giriniz : ")
            numara = input("Yeni Numarayi Giriniz : ")
            guncellenen[ad]=numara      #Yeni girilen yani guncellenen bilgileri actigimiz ikinci sozluge gonderdik
            veritabani.update(guncellenen)      # ikinci sozluktekileri ana veritabanimiza gonderdik.
            print(veritabani)
            islem2 = input( """Guncelleme Islemine Devam Etmek Icin ENTER' a Basiniz, Bir Ust Menuye Donmek Icin baska bir tusa  Basiniz! : """.upper())
            if islem2 == "":
                continue
            else:
                break


        if islem=="4":
            if veritabani!="":
                print(veritabani)
                a=input("Bir Ust MEnuye Donmek Icin HErhangi Bir Tusa BAsiniz !")
                break
            if not veritabani:
                print("Liste Bos\n")
                break







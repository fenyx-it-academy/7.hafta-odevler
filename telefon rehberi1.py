rehber={}



with open("rehber.txt", "a+") as oku:
    oku.seek(0)
    for i in oku:        
        i=i[0:-1]       
        i=i.split(":")        
        rehber[i[0]]=i[1]
        
    
while True:

    print("TELEFON REHBERI UYGULAMASI")


    menu = input("""    1- Kisi Ekle
    2- Kisi Silme
    3- Kisi Bilgi Guncelleme
    4- Rehber Listeleme
    5- Dosya Kayıt
    6- Cikis
    
    Lutfen Yapmak Istedeginiz Islemin Numarasini Giriniz  : """)
    cikis=0

    if menu=="1":
        while cikis == 0:
            isim    = input("Isim giriniz :").upper()
            soyisim = input("Soyisim giriniz :").upper()
            tel_no  = input("Telefon Numarasi :")
            rehber[isim+ " " + soyisim]=tel_no

            cikis = int(input("Tekrar isim eklemek icin 0 / Ana Menu icin 1 tusunu giriniz :"))


    elif menu=="2":
        print("REHBERDEN ISIM SILMEK ICIN ISIM VE SOYISIM BILGILERI AYRI AYRI GIRILECEKTIR\n")
        isim_sil    = input("Lutfen Silmek istediginiz ismi giriniz : ").upper()
        soyisim_sil = input("Lutfen Silmek istediginiz soyismi giriniz : ").upper()
        anahtar = isim_sil+" " + soyisim_sil
        print(rehber.pop(anahtar,"Bu isim ve soyisim rehberde bulunmamaktadir.\n"))
    elif menu=="3":
        isim_deg = input("Lutfen ismi giriniz :").upper()
        soyisim_deg = input("Lutfen soyismi giriniz :").upper()
        tel_no_deg = input("Lutfen yeni telefon numarasini giriniz : ")
        anahtar = isim_deg + " " + soyisim_deg

        if anahtar in rehber:
            rehber[anahtar]= tel_no_deg
        else:
            print("Bu isim ve soyisim rehberde bulunmamaktadir.")



    elif menu=="4":
        liste = list(rehber.items())
        
        print("\n")
        for a,b in liste:
            print(a," : ",b)
        print("\n")
    elif menu=="5":
        with open("rehber.txt", "w") as r:
            liste = list(rehber.items())
            for a,b in liste:
                r.write(a + ":" + b+ "\n")
        print("\nDosyaya Basari ile kaydedilmistir...\n")

    elif menu=="6":
        quit()

    else:
        print("\nLutfen gecerli bir menu secenegi giriniz ....\n")





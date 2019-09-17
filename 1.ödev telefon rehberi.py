print("***telefon rehberine hoş geldiniz lütfen yapmak istediğiniz işlemi seçiniz***")
while True:
    print("""
    (1) kişi ekleme ve silme
    (2) kişi isim veya numara güncelleme
    (3) rehberinizi listeleyin
    (4) çıkış
    """)

    rehber = {}
    güncel = {}
    işlem=input("lütfen yapmak istediğiniz işlemi seçiniz:")

    if işlem=="1":
        print("""
        (a) kişi ekleme
        (b) kişi silme
        """)
        seçim=input("lütfen yapmak istediğiniz işlemi seçiniz:")
        if seçim == "a":
            isim = input("lütfen kaydetmek istediğiniz ismi giriniz:")
            numara = input("lütfen kaydetmek istediğiniz numarayı giriniz:")
            rehber[isim] = numara
        elif seçim == "b":
            isim = input("lütfen silmek istediğiniz ismi giriniz:")
            rehber.pop(isim)
            
            
    elif işlem == "2":
        isim = input("lütfen güncellemek istediğiniz ismi giriniz:")
        numara = input("lütfen güncellemek istediğiniz numarayı giriniz:")
        rehber[isim] = numara
        rehber.update(güncel)
        print(rehber) 
    elif işlem == "3":
        for i in rehber:
            print(i)
    elif işlem == "4":
        print("rehberden çıkılıyor...")
        break

    with open("C:/python ödevleri/7.hafta ödevleri/rehberim.txt","w+",encoding="utf-8")as rehberim: 
        for k, v in rehber.items():
            rehberim.write(str(k) + "=" + str(v) + "\n")
        rehberim.close()
        

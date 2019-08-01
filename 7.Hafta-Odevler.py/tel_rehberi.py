"""telefon rehberi uygulamasi
Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme,
rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
Olusturulan rehberi bir dosyaya kaydedin.
Rehberi olustururken sozlukleri kullanin."""
telefon_rehberi = {"python":"065667788",
          "jango":"0635478632",
          "php":"065276896542",
          "java":"06387652829"}
secenekler = """Telefon rehberi uygulamasini kullanmak icin asagidaki secenekleri seciniz,
(1)kisi ekle
(2)kisi sil 
(3)isim yada tel guncelle
(4)rehberi listele
(q)cikis
"""
guncel = {}
while  True:
    try:
        islem = input("yapmak istediginiz islemi seciniz: ")
        if islem =="1":
            kisi = input("eklemek istediginiz kisinin isimini girin: ")
            telefon = input("eklemek istediginiz kisinin telefonunu giriniz: ")
            telefon_rehberi[kisi] = telefon
            print(telefon_rehberi)
        elif islem =="2":
            kisi = input("silmek istediginiz kisinin ismini girin: ")
            print(telefon_rehberi.pop(kisi, "listenizde boyle birisi yok"))
            print(telefon_rehberi)
        elif islem == "3":
            for i in range(len(telefon_rehberi)):
                kisi = input("guncellemek istediginiz kisinin ismini girin: ")
                telefon = input("guncellemek istediginiz kisinin telefonunu girin: ")
                guncel[kisi] = telefon
                telefon_rehberi.update(guncel)
                print(telefon_rehberi)

        elif islem =="4":
            for isim,telefon in telefon_rehberi.items():
                print("{} = {}".format(isim,telefon))
        elif islem == "q":
            break
    except:
        print("bir hata olustu")

dosya = open("rehber.txt", "w")

for k,v in telefon_rehberi.items():
    dosya.write(str(k) + ">>" + str(v) + "\n\n")
dosya.close()
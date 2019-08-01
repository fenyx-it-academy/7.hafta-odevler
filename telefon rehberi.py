#telefon rehberi uygulamasi
#Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
#Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme, 
#rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
#Olusturulan rehberi bir dosyaya kaydedin.
#Rehberi olustururken sozlukleri kullanin.
telefon_rehberi=("1.kayıt\n2.kişi silme\n3.kişi güncelleme\n4.rehberi listeleme\n5.çıkış")
print(telefon_rehberi)

rehber={}
print("\ntelefon rehberine hoş geldiniz!!\n")
while True:
    secim=input("seciminiz:")
    if secim=="1":
        #print("mevcut olan kişiyi değiştir veye yeni kişi olustur.")
        tel_no=input("yeni kişi oluşturmak için telefon numarasını giriniz:")
        adı_soyadı=input("yeni kişinin adını ve soyadını giriniz:")
        rehber[adı_soyadı]=tel_no
        print(adı_soyadı," adlı kişi kaydedildi...")
    #else:
        #print("sadece sayı giriniz")
        #continue
    if secim=="2":
        sil=input("silmek istediginiz kişi'nin ad-soyad giriniz:")
        a=(input("adlı kişi silinsin mi?\nsilmek için 2'ye basınız:\nvazgeçmek için 1'e basınız:")).lower()
        #print(rehber.pop(sil,"rehberde böle birisi yok.."))
        if a =="2":
            print(rehber.pop(sil,"silinecek kişi bulunamadı"))
            #print(rehber.pop(sil,"adlı kişi silindi.."))
        elif a=="1":
            #rehber.pop(sil)
            print(sil,"silmekden vaz geçtiniz")
        else:
            #rehber.pop(sil,"böyle bir kişi bulunamadı")
            print("yanlış giriş yaptınız tekrar deneyin...")
        continue
    if secim=="3":
        güncel=input("güncellemek istediğiniz kişinin ad soyadını giriniz:")
        for y in rehber.keys():
            if y == güncel:
                adı_soyadı1=input("yeni ad-soyad:")
                tel_no1=input("yeni telefon numarası:")
                rehber[adı_soyadı1]=tel_no1
                rehber.pop(güncel)
                print(rehber)
                print(güncel,"kişi güncellendi")
            else:
                print("böyle bir kişi telefon rehberinde bulunamadı")
        break
    if secim=="4":
        rehber.items()
        for anahtar,değer in rehber.items():
            print("{}={}".format(anahtar,değer))
            continue
    if secim=="5":
        çıkış=input("çıkmak için q'basınız:")
        print("çıkılıyor....")
        break
dosya_kayıt=open("telefon\trehberi.txt","w")
dosya_kayıt.write("adı_soyadı\tnel_no\n")
for k,v in rehber.items():
    dosya.write(a)
dosya.close()
    
        
        
        
                




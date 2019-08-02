##telefon rehberi uygulamasi
##Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
##Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme, 
##rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
##Olusturulan rehberi bir dosyaya kaydedin.
##Rehberi olustururken sozlukleri kullanin.


rehber={'Mehmet':'1234','Ayse':'4321','Ali':'6789','Orhan':'9876'}              ##Onceden rehbere oylesine iki isim eklendi 
guncel={}
islem=['1','2','3','4','q']                                                     ##islem basamaklarini takip icin liste olusturuldu
harf="azxcvbnm,./';lkjhgfdsqwertyuiop1234567890"
harf2="azxcvbnm,./';lkjhgfdsqwertyuiop"
rakam="1234567890"

while True:
                                            
    kul=input("Rehbere kisi eklemek icin 1'e, kisi silmek icin 2'ye, kisi guncellemek icin 3'e, arama yapmak icin 4'e, cikmak icin q'ye basiniz : ")       
    if kul !='1' and kul !='2' and kul !='3' and kul !='4' and kul !='q':           ##sadece liste iceriginin girilmesi saglandi  
        print("lutfen belirtilen rakamlardan en az bir tanesini giriniz!!")
        
    if kul=='1':
        isim=input("Lutfen isim giriniz: ")
        tel=input("Lutfen tel no giriniz: ")
        for i in tel :
            if i not in rakam:
                print("Lutfen sadece rakam giriniz!!")
                quit()
        rehber[isim]=tel       
        print("\n")
        for oge in rehber:
            print(oge)
        print("\nTum liste: ",rehber)
        print("\n")
    if kul=='2':
        silinecek_isim=input("Silinecek ismi giriniz : ")
        if silinecek_isim not in rehber:                                        ##yanlis isim yazilmasi onlendi
            print("Lutfen ismi dogru yazdiginizdan emin olunuz!!")
            silinecek_isim=input("Silinecek ismi giriniz : ")
        silinecek_numara=input("Silmek istediginizden eminmisiniz? e/h) : ")
        if silinecek_numara=="e":
            print("siliniyor..")
            rehber.pop(silinecek_isim,silinecek_numara)
        if silinecek_numara=="h":
            print("isleminiz devam ediyor..")                             
        print("\n")
        for oge in rehber:
            print(oge)
        print("\nTum liste: ",rehber)
        print("\n")
    if kul=='3':
        guncellenecek_isim=input("Guncellenecek ismi giriniz : ")
        if guncellenecek_isim not in rehber:
            print("Lutfen ismi dogru yazdiginizdan emin olunuz!!")
            guncellenecek_isim=input("Guncellenecek ismi giriniz : ")
        guncellenecek_numara=input("Guncellenecek numarayi giriniz (bilmiyorsaniz bos birakiniz) : ")
        rehber.pop(guncellenecek_isim,guncellenecek_numara)                             ##pop ile onceki degeri silindi
        rehber[input("Guncel ismi giriniz : ")]=input("Guncel numarayi giriniz : ")     ##rehber['keys']=['value']  ile yeni degerleri rehbere eklendi
        
##            guncel={input("Guncel ismi giriniz : "):input("Guncel numarayi giriniz : ")}      ##istersek bu sekildede yeni degerleri atayabiliriz
##            rehber.update(guncel)
        print("\n")
        for oge in rehber:
            print(oge)
        print("\nTum liste: ",rehber)
        print("\n")
    if kul=="4":
        aranan_isim=input("Aramak istediginiz ismi giriniz : ")
        sonuc=rehber.get(aranan_isim)
        print("\n")
        print(aranan_isim, "\'in tefon numarasi : ",sonuc)
        print("\n")
        for oge in rehber:
            print(oge)
        print("\nTum liste: ",rehber)
        print("\n")
    if kul=="q":
        break
    
       
  
    
        
               









            
        

#rehber1 ve rehber2 , ad-numara, numara -ad şeklinde iki farklı küme
rehber1={}
rehber2={}
dosyarehber=open("C:/Users/Admin/Desktop/telefonrehberi.txt", "r" )
dosyarehber.seek(0)
oku=dosyarehber.read()
toplulist=oku.split("---")

# dosyadaki bilgiler kümelere aktarılır
for i in toplulist:
    if toplulist.index(i)%2==0:
        ad=i
    else:
        no=i
        rehber1[ad]=no
        rehber2[no]=ad
dosyarehber.close()

##
##
kisi_sy=0
a=1
while a==1:

    secim=input("Telefon Rehberine Hoş Geldiniz\n\nLütfen aşağıdaki uygulamalardan hangisini seçmek"
                " isterseniz yanındaki numaralı tuşa basınız\n(1)Kişi ekleme\n(2)Numara ekleme\n(3)Kişi güncelleme\n"
                "(4)Numara güncelleme\n(5)Rehber görüntüleme\n(q)KAYIT / ÇIKIŞ\n")
    if secim=="1" or secim=="2" or secim=="3" or secim=="4" or secim =="5":
        if secim=="1":
            isim=input("lütfen eklemek istediğiniz ismi giriniz..")
            numara=input("Lütfen Tel no ekleyin")
            rehber1[isim]=numara
            rehber2[numara]=isim


            print("Kaydınız başarı ile gerçekleşmiştir")

            continue
        #
        if secim=="2":
            numara=input("Lütfen Tel no ekleyin")
            isim = input("lütfen eklemek istediğiniz ismi giriniz..")
            rehber1[isim]=numara
            rehber2[numara]=isim

            print("Kaydınız başarı ile gerçekleşmiştir")

            continue
        
        if secim=="3":
            isim = input("lütfen düzeltmek istediğiniz ismi giriniz..")
            if isim not in rehber1:
                print("Bu isim rehberde yok")
                continue
            else:
                y_isim=input("Lütfen yeni ismi girini")
                no_yedek=rehber1[isim]
                rehber2[no_yedek]=y_isim
                rehber1[y_isim]=rehber1.pop(isim)  

        if secim=="4":
            print(rehber2)
            no = input("lütfen düzeltmek istediğiniz noyu giriniz..")

            if no not in rehber2:
                print("Bu no rehberde yok")
                continue
            else:
                y_no=input("Lütfen yeni no giriniz")
                isim_yedek=rehber2[no]
                rehber1[isim_yedek]=y_no
                rehber2[y_no]=rehber2.pop(no)        

        if secim=="5":
            for i in rehber1:
                print("{:14}:{}".format(i,rehber1[i]))


    elif secim=="q" or secim =="Q":
        break
    else:
        print("Lütfen sizden istenilen seçimi yapınız")
dosyarehber=open("C:/Users/Admin/Desktop/telefonrehberi.txt", "w" )
for i in rehber1:
    kayıt=i+"---"+rehber1[i]+"---"
    dosyarehber.write(kayıt)
    
dosyarehber.close()


    


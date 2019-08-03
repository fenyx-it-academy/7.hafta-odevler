##*TO DO LIST*
##-Yapilacaklar listesi ve yapilanlar listesi seklinde iki bos liste olusturun. Kullanicinin yapabilecegi islemler:
##   *Yapilacaklar listesine gorev ekleme
##       ->append metodu kullanilsin
##   *Yapilacaklar listesinden gorev silme
##       -> del metodu kullanilsin
##   *Yapilacaklar listesindeki gorevi yapilanlar listesine atama
##       -> pop metodu kullanilsin
##   *Yapilanlar listesini goruntuleme
##   *kullanıcı yapılacaklar listesinin içini boşaltma
##       -> clear metodu kullanılsın
##-Dongu her basa dondugunde yapilacaklar listesi goruntulensin
##-Her iki liste goruntulenirken liste elemanlari numaralandirilarak verilsin
##   ORN:
##       Yapilacaklar Listesi:
##           1- Python odevini yap.
##           2- Alis-veris yapmaya git.
##           3- Ahmet'i ara.
##- Eger yapilacaklar listesi bos ise "Su an yapilacaklar listeniz bos" seklinde bir cikti versin.


Yapilacaklar=["YEMEK YAPILACAK", "ODEV YAPILACAK", "CANTA HAZIRLANACAK", "EVE TELEFON EDILECEK"]
Yapilanlar=[]
print(15*"0","TO DO list programi", 15*"0")
while True:
  menu=input("""    Listeye gorev eklemek icin------->1
    Listeden gorev silmek icin ------>2
    Listeyi tum bosaltmak icin------->3
    Listedeki gorevi \"Yapilanlar\" listesine gondermekmek icin------>4
    Yapilanlar listesini gormek icin ------>5
    Cikmak icin---------------------->6
    \ttuslayiniz:""")
  menu=int(menu)
  if menu == 1:
    Gorev=input("Yapacaginiz gorevi giriniz:")
    Yapilacaklar.append(Gorev)
    print(Gorev, ":\tgorevi basariyla listeye eklenmisir.")
    print("Yeni gorev listesi su sekildedeir.")
    for öğe_sırası in range(len(Yapilacaklar)):
        print("{}- {}".format(öğe_sırası+1, Yapilacaklar[öğe_sırası]))
    continue
  elif menu==2:
      for öğe_sırası in range(len(Yapilacaklar)):
        print("{}- {}".format(öğe_sırası+1, Yapilacaklar[öğe_sırası]))
      secim=input("Yukarda listelenen gorevlerden silmek istediklerinizin numarasini giriniz:")
      silinecek=Yapilacaklar[int(secim)-1]
      Yapilacaklar.remove(silinecek)
      print(silinecek, "gorevi listeden silinmistir.\n Yeni Yapilacaklar listesi asagidaki gibidir.")
      for öğe_sırası in range(len(Yapilacaklar)):
        print("{}- {}".format(öğe_sırası+1, Yapilacaklar[öğe_sırası]))
        continue
  elif menu==3:
    Yapilacaklar.clear()
    print("Yapilacaklar listeniz bom bos")
    continue
  elif menu==4:
      for öğe_sırası in range(len(Yapilacaklar)):
          print("{}- {}".format(öğe_sırası+1, Yapilacaklar[öğe_sırası]))
          continue
      secim=input("Yukarda listelenen gorevlerden hangisini \"Yapilanlar\" klasorune gondermek istersiniz onun numarasini giriniz:")
      Yapilanlar+=[str(Yapilacaklar[int(secim)-1])]
      gidecek=Yapilacaklar[int(secim)-1]
      Yapilacaklar.pop(int(secim)-1)
      print(gidecek, "gorevi Yapilanlara eklenmistir.\n Yeni Yapilacaklar ve Yapilanlar listesi asagidaki gibidir.")
      print("YAPILACAKLAR")
      for öğe_sırası in range(len(Yapilacaklar)):
          print("{}- {}".format(öğe_sırası+1, Yapilacaklar[öğe_sırası]))
          continue
      print("YAPILANLAR")
      for sira in range(len(Yapilanlar)):
          print("{}- {}".format(sira+1, Yapilanlar[sira]))
          continue
  elif menu==5:
    print("YAPILANLAR")
    for sira in range(len(Yapilanlar)):
          print("{}- {}".format(sira+1, Yapilanlar[sira]))
          continue
  elif menu==6:
    print("PROGRAM KAPANIYOR....IYI GUNLER.")
    break
          

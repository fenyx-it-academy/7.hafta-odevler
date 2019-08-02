print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


with open("Rehberlik.txt", "r+", encoding="utf-8") as file:
    file.seek(0)                                    #bastan itibaren okusun
    satir = file.readlines()
rehber = {}

for c in satir:
    harf = c.split(":")                 #her satirda kisi ve numara arasinda : isaretinden ikiye ayirip iki indeksli liste olusturuldu
    rehber[harf[0]] = harf[-1]          # : dan onceki kisim key ve sonrasi value. her satiri rehber sozlugune ekledik


while True:
    kisi = input("Aramak istediginiz kisinin adini giriniz: ").upper()
    print(rehber.get(kisi, f"{kisi} adli kisi telefon rehberinizde bulunmamaktadir."))  # kisinin rehberde var olup olmadigini veriyor

    process = input("Islem yapmak isterseniz 'Y' istemiyorsaniz 'N' tiklayiniz: ").upper()
    if process == "N":
        print("Cikiliyor...")
        break
    elif process == "Y":

        komut = input("""Hosgeldiniz... Islem listeniz asagida belirtilmistir.
        1 - Rehbere kisi eklemek,
        2 - Rehberden kisi silmek,
        3 - Isim veya Telefon numarasi guncelleme,
        4 - Rehberi liste seklinde gostermek.
        5 - Cikis

        Lutfen yapmak istediginiz islemin numarasini giriniz: """)
        try:
            if komut == "1":
                keys = input("Eklemek istediginiz kisinin adini giriniz: ").upper()
                if keys not in rehber:                                          #isim rehberde kayitliysa
                    value = input("Lutfen telefon numarasini giriniz: ")
                    rehber[keys] = value
                    print(keys + "   : " + value, "kaydedildi.")
                else:                                                           #isim kayitli degilse
                    print("Bu kisi kayitlidir.")
                    yinede = input("Devam etmek istiyorsaniz 'E' giriniz: ").upper()
                    if yinede == "E":
                        value = input("Lutfen telefon numarasini giriniz: ")
                        rehber[keys] = value
                        print(keys + "   : " + value, "kaydedildi.")
                    else:
                        print("Bir onceki menuye geciyorsunuz.")

            elif komut == "2":
                keys1 = input("Silmek istediginiz kisinin adini giriniz: ").upper()
                rehber.pop(keys1, "Silinecek kisi listenizde bulunmamaktadir!")  # eleman varsa siliyor yoksa uyariyor
                for keys, value in rehber.items():
                    print(f'{keys}:{value}')

            elif komut == "3":
                hangi = input("Isim guncellemek icin 'I', Numara guncellemek icin 'N' giriniz: ").upper()
                if hangi == "I":
                    isim = input("Guncellemek istediginiz kisinin adini giriniz: ").upper()
                    new_name = input("Guncel isim giriniz: ").upper()
                    rehber[new_name] = rehber.pop(isim)
                    print(rehber)

                elif hangi == "N":
                    isim = input("Guncellemek istediginiz kisinin adini giriniz: ").upper()
                    for i in rehber.keys():                                     # rehberde olmayan birini guncellemek
                        if i in isim:                                           #isim varsa guncelle
                            no = input("Guncel telefon numarasini giriniz: ")
                            rehber[isim] = no
                            print(rehber)
                        else:                                                   #rehberde isim yoksa veya yanlis girildiyse
                            print("Lutfen guncellemek istediginiz ismi giriniz!")
                            break

            elif komut == "4":                                                      # liste gosterimi
                for i in rehber.items():
                    print(*list(i), sep=":", end="\n")

            elif komut == "5":
                print("Islemden cikiliyor...")
                quit()
            else:
                print("Hatali giris yaptiniz!")
        except (KeyError, ValueError):
            print("Hatali giris yaptiniz!")

with open("Rehberlik.txt", "w") as file1:
    for v in rehber:
        cikti = f'{v}:{rehber[v]}' + "\n"
        file1.write(cikti)

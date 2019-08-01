print("\nSIFRELEME PROGRAMI")                                                       # imza sablonumuzun ilk satirini yazdik
print("-" * 5, "ZAFER", "-" * 5, end="\n\n")                                        # imza sablonumuzun ikinci satirini yazdik
                                                                                    # kullaniciya karsilama metni ve menuyu sunduk
print("""Sifreleme Programimiza hosgeldiniz.                                        
Lutfen asagidaki menuye gore isleminizi seciniz\n
    Metin sifreleme                 1
    Sifreyi metne donusturme        2
    Cikis                           3
""")

import time                                                                         # bekletmeler icin zamani cagirdik
                                                                                    # sozlugumuzu olusturduk
sozluk={
    'Istanbul'  :   'A1B8',
    'Ankara'    :   'V29x',
    'Izmir'     :   '43hG',
    'Adana'     :   'y_4N',
    'Erzurum'   :   'RF5.',

    'AVM'       :   '4q6z',
    'Otogar'    :   'KW07',
    'Kampus'    :   'li=8',
    'Cami'      :   'jKS9',

    'Sabah'     :   'B1n0',
    'Oglen'     :   'U1p7',
    'Ikindi'    :   'O12e',
    'Aksam'     :   '1k3t',
    'Yatsi'     :   'iq%4'
}
                                                                                    # programda kullanacagimiz listeleri belirledik
list_sifre=[]
list_metin=[]


while True:                                                                         # hatali veri girisine karsi dondugumuzu olusturduk
    islem = input("Lutfen yapmak istediginiz islemi seciniz : ")

    if islem == '1' or islem == '2' or islem == '3':
        break
    else:
        print("\nLutfen menudeki seceneklere uygun tercih yapiniz.\n")
        continue

if islem == "1":                                                                                              # kullanicinin metni sifrelemek istemesi secenegini yazdik
    metin=input("\nLutfen sifrelemek istediginiz metni kelimeler arasinda birer bosluk birakarak giriniz : ")   # kullanicidan metni aldik
    for k, v in sozluk.items():                                                                                 # aldigimiz metnin sozlukteki karsiligini bulmak icin gereken kodlari yazdik
        if k in metin:
            list_sifre.append(v)                                                                                # metnin sozlukteki karsiligini yukarda olusturdugumuz listeye yazdik
    print("\nMetninizin sifresi : ", *list_sifre)                                                               # sifreyi kullaniciya gosterdik
    print("\nBu program 3 sn icinde herseyi imha edecektir.")
    time.sleep(3)
    print("Imha islemi tamamlanmistir. Artik hicbir veriye ulasamazsiniz :(")

elif islem == "2":                                                                                              # kullanicinin sifreyi metne donusturmek istemesi secenegini yazdik
    sifre = input("\nLutfen metne donusturmek istediginiz sifreyi giriniz : ")                                  # kullanicidan sifreyi aldik
    for k, v in sozluk.items():                                                                                 # aldigimiz sifrenin sozlukteki karsiligini bulmak icin gereken kodlari yazdik
        if v in sifre:
            list_metin.append(k)                                                                                # sifrenin sozlukteki karsiligini yukarda olusturdugumuz listeye yazdik
    print("\nSifrenizin metni : ", *list_metin)                                                                 # sifreyi kullaniciya gosterdik
    print("\nBu program 3 sn icinde herseyi imha edecektir.")
    time.sleep(3)
    print("\nImha islemi tamamlanmistir. Artik hicbir veriye ulasamazsiniz :(")

elif islem == '3':                                                                                              # kullanicinin programdan cikmak istemesi secenegini yazdik
    print("\nProgramdan cikiyorsunuz...")
    time.sleep(2)
    print("\nProgramdan ciktiniz.")
    quit()

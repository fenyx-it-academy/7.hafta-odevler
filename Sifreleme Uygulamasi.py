# Girilen metinleri harf harf key olarak,
# her harf icin olusturacagimiz random karakterleri de
# value olarak kaydedecegimiz sozlugu tanimladik.
passDictionary={
}

# Girilen metinleri ve sifrelenmis hallerini butun olarak
# kaydedecegimiz sozlugu tanimladik.
myPasswords = {
}

import string
import random

print('*'*30+'\n\n'+'Sifreleme Uygulamasi'.rjust(22)+'\n\n'
      +'1.Metni Sifrele\n'+'1.Sifreli Metni Coz\n\n'
      +'Cikis icin "q" ya basin!\n\n'+'*'*30)

#kullanicin sectigi islemi atayacagimiz degisken
islem = ''

# Girilen metin tekrar girilmis mi diye kontrol etmek icin
# tum keyleri ve value lari ekleyecegimiz listeler
keysList=[]
valuesList=[]

try:
    while islem != 'q':
        # print('_' * 30 + '\nSifre Veritabani:')

        #Tum metinler ve sifrelerin oldugu sozlugu ekrana yazdirdik
        # for key, value in myPasswords.items():
        #     print(key + ' >>> ' + value)
        print('_' * 30)
        islem = input('Yapmak istediginiz islemi secin: ')

        if islem == '1':
            str = input("Sifrelemek istediginiz metni girin: ")

            if str in keysList:
                #girilen metin keyListte mevcut ise daha once sifrelendigi icin tekrar sifrelenmez
                print('_' * 30 + '\nGirmis oldugunuz metin daha once sifrelenmis !!')
            else:
                #buyukharf,kucukharf ve rakamlardan olusan bir string
                sifre = string.ascii_uppercase + string.ascii_lowercase + string.digits

                sifrelenmisMetin = ''
                a = range(len(str))

                for i in a:
                    #yukarida olusturdugumuz kapsamli stringin icinden random bir karakter seciyoruz
                    randomChar = ''.join(random.choice(sifre))

                    #girilen stringi ve secilen random karakterleri teker teker key : value olarak
                    #password sozlugumuze kaydediyoruz
                    passDictionary.update({str[i]: randomChar})

                    #girilen metindeki karakterlerin olusturdugumuz sozlukteki karsiliklarini
                    #sifrelenmisMetin degiskenine aktariyoruz
                    for key, value in passDictionary.items():
                        if str[i] == key:
                            sifrelenmisMetin += passDictionary[key]

                #girilen metin ile sifrelenmis halini password veritabanimiza kaydediyoruz
                myPasswords.update({str: sifrelenmisMetin})

                #onceden girilip girilmedigini kontrol edebilmek icin olusturdugumuz
                #listelere key ve value elemanlarini atiyoruz
                for key, value in myPasswords.items():
                    keysList.append(key)
                    valuesList.append(value)

                print('Girdiginiz metin basarili bir sekilde sifrelendi. Sifre: ', sifrelenmisMetin)
        elif islem == '2':
            str2 = input('Cozmek istediginiz sifreyi girin: ')

            #cozulmek istenen sifre veritabaninda mavcut mu?
            if str2 in valuesList:
                for key, value in myPasswords.items():
                    #girilen sifreli metnin sozlukteki karsiligini sorguladik
                    if value == str2:
                        print('_' * 30)
                        print('Girdiginiz sifrenin orjinali: {}'.format(key))
            else:
                print('_' * 30 + '\nGirmis oldugunuz sifre veritabaninda mevcut degil !!')
        else:
            print('Gecerli bir islem secin!')
except:
    print('Hatali islem!')

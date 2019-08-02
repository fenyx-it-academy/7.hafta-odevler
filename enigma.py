# coding=utf-8
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':''}
print ('''Enigma programı ile metinlerinizi şifreleyebilir 
veya şifreli metinleri çözümleyebilirsiniz.
Metin şifrelemek için 1 e
şifreli metinleri çözümlemek için ise 2 ye basınız.
Programdan çıkmak için ise q ya basınız.''')

while True:
    secim=input('Hangi islemi yapmak istersiniz? ')

    if secim=='1': #sifreleme girisi
        enigma=''  #harflerin mors karakteri olarak tutulacagı degisken
        metin=input('Şifrelemek istediğiniz metni yazınız.').upper() # sifrelenecek metin girisi ve buyuk harfe donusturme

        for i in metin: #  girilen metindeki her harf icin dongu
            enigma+=MORSE_CODE_DICT[i]  # harfin sozlukten degerini bulup degiskene atama
            enigma+=' '  # harfi temsil eden herbir mors kodu arasına boluk ekleme
        print (enigma)

    elif secim=='2': # kod çözümleme girişi
        kod=input('Çözümlemek istediğiniz kodu yazınız.') #kod giris
        mors_karakter='' #bir harfe krsılık gelecek bir mors sifresindeki herbir karakterin tutulacagı degisken
        mors_harf='' #kodun harfe desifre edildiginde tutulacagı degisken

        for karakter in kod:
            if karakter!=' ': # kod icinde bosluk gelene kadar semboller degiskene biriktirilir
                mors_karakter+=karakter
                i=0

            elif karakter==' ': #bosluk varsa bir harflik mors sembolleri tamamlandı demektir.
                i+=1 #sayac karakter degsikeninin art arda kac bosluk gordüğünü kontrol amaclı

                if i==2: # bir bosluk harfleri,iki bosluk kelimeleri ayırır. iki boluk art arda geldiyse durumu
                    mors_karakter='' # sozluge ' ':'' eklendi
                mors_harf+=list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mors_karakter)]
                mors_karakter='' #degisken sıfırlanır
        print (mors_harf)

    elif secim=='q':
        print ('Program kapatılıyor.')

    else:
        print ('Yanlış giriş yaptınız. Sizden istenen seçeneklerden birini giriniz.')




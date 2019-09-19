
harfler='qwertyuiopasdfghjklzxcvbnm'
harfler2='mlpoknjiuhbvgytfcxdreszaqw'
karakterler='1234567890[]{}|":<>?!@#$%^&*\'()_+\\;,./=-'
karakterler2='+_)(*&^%$#@!=-0987654321}{|":<>?/.,;\'[]\\'
#kullanicinin girebilecegi harfeleri ve karakterleri degisken olusturduk
#ikinci degiskende yerlerini degistirerek yazdik ve for dongusu yardimiyla
#bunlari bi sozluk haline getirdik for dongusu bunu yaparken bi siraya gore
#yapti fakat degiskenler farkli oldugu sifreleme icin simdilik uygun sozlugu elde ettik
sifre={' ':' '}
#sifre adi sozluge bosluk karakterini onden tanimladim cunku
#eger kullanici bosluk bulunan bir metin girerse bu kodlama bakimindan
#daha uzun surdugu icin bunu direk sozluge ekleyerek yaptim
print('Sifreleme programina hos geldiniz...')
for i in harfler :
    sifre[i]=harfler2[harfler.index(i)]
for i in karakterler :
    sifre[i]=karakterler2[karakterler.index(i)]
# for x,y in sifre.items() :
#     print('{}:{}'.format(x,y))
#burda ki for dongusu eger sozlugu goruntulemek isterseniz diye
#etkisiz bi sekilde biraktim
while True :
    secim=input('Lutfen sifreleme yapmak icin 1\'e\
sifrelemeyi cozmek icin 2\'ye basiniz\
 cikmak icin lutfen q\'ya basiniz:')
    girdi = ''
    if secim=='q':
        print('Programdan cikiliyor!')
        break
    if secim=='1' :
        metin=input('Lutfen sifrelemek istediginiz metini giriniz')
#eger kullanici metin sifrelemek isterse bu metni input ile alip
#daha sonra for yardimiyla her harfin sozlukte ki karsiligini
#girdi adli bi degiskene atadik ve sifrelenmis halini printle verdik
        for i in  metin :
            girdi+=sifre[i]

        print(girdi)
    if secim=='2' :
        metin=input('Lutfen cozmek istediginiz metini giriniz:')
#eger kullanici bir sifrelenmis metni normal hale gerimek isterse
#for dongusu ile once metindeki her harfe bakiyor daha sonra
#sozlukteki her iteme bakiyor ve bunu iki farkli degiskene atiyor
#gelen metin bizim sozlugumuzdeki values karakterleri oldugu icin
#for dongusu ile metin ile values eslestiginde bunun key degerini
#vermesini istedik ve bunu printle ekrana yazdirdik
        desifre=''
        for i in metin :
            for x,y in sifre.items() :
                if i==y :
                    desifre+=x


        print(desifre)




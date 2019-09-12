print('b.')
'''
Şifreleme Uygulaması
Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve
sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz. 
Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve
kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin ve ekrana yazdirin. 
Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal metne ulasabilsin.
'''
sifre={'a':'~',
       'b':'!',
       'c':'@',
       'd':'#',
       'e':'$',
       'f':'%',
       'g':'^',
       'h':'&',
       'i':'*',
       'j':'(',
       'k':')',
       'l':'|',
       'm':',',
       'n':'=',
       'o':'+',
       'p':'?',
       'r':'.',
       's':';',
       't':'<',
       'u':'>',
       'v':'/',
       'y':'`',
       'z':'-',
       ' ':' '}
while True:
    secim='''
    1-sifre olusturmak icin (1)
    2=sifre cozmek icin (2)
    3-cikis icin (3)
    '''
    print(secim)
    cvp=input('\nne yapmak istiyorsunuz?')
    if cvp =='1':
        bilgi=input('\nsifrelemek istediginz bilgiyi yaziniz\n'
                    '(not:rakam kullanmayiniz rakamlari harf ile yazabilirsiniz)').lower()
        if bilgi.isalpha():     #girilen bilginin icersinde rakam varmi kontrol ettik
            bilgi_lis=[]
            for bilgi_harf in bilgi:
                bilgi_lis.append(sifre[bilgi_harf])   #girilen bilginin harflerini listeye ekledik
            print('sifre...:\n',*bilgi_lis,sep='')
        else:
            print('\n!!!HATA!!!lutfen icersinde rakam olmayan bir deger giriniz\n'
                  'not:rakamlari harf ile yazabilirsiniz')
    elif cvp=='2':
        cozm_list = []
        key_list  = []
        value_list = []
        sifre_list = []
        for sifre_key, sifre_value in sifre.items(): #sifremizdeki key ve value degerlerini listeye cevirdik
            key_list.append(sifre_key)
            value_list.append(sifre_value)
        coz = input('cozmek istediginiz sifreli metni giriniz ....>\n')
        for coz_harf in coz:            #sifreli metnini listeye donusterduk
            sifre_list.append(coz_harf) #karekterleri sifre_list ekledik

        for sifre_harf in sifre_list:
            # sifreli her degerin index nosunu bulup,index nolara karsilik gelen anahtarlara ulastik
            key_harf = key_list[value_list.index(sifre_harf)]
            cozm_list.append(key_harf)
        print(*cozm_list,sep='')
    elif cvp=='3':
        print('cikiliyor')
        quit()

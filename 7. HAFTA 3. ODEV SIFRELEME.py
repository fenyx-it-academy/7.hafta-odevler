'''Şifreleme Uygulaması
Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve
 sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz.
Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve
 kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin
ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input olarak
yazdiginda orjinal metne ulasabilsin.'''

sifreleyici={'A':'!', 'B':'@',
             'C':'#', 'D':'$', 'E':'$',
             'F':'%', 'G':'^', 'H':'&',
             'I':'*', 'J':'(', 'K':')',
             'L':'-', 'M':'_', 'N':'+',
             'O':'1', 'P':'2', 'Q':'3',
             'R':'4', 'S':'5', 'T':'6',
             'U':'7', 'V':'8', 'W':'9',
             'X':'0', 'Y':'|', 'Z':'"',
             'a':'M', 'b':'N',
             'c':'B', 'd':'V', 'e':'C',
             'f':'X', 'g':'Z', 'h':'L',
             'i':'K', 'j':'A', 'k':'S',
             'l':'D', 'm':'F', 'n':'G',
             'o':'H', 'p':'J', 'q':'T',
             'r':'Y', 's':'U', 't':'I',
             'u':'O', 'v':'P', 'w':'Q',
             'x':'E', 'y':'W', 'z':'R',
             '1':',', '2':'.', '3':'/',
             '4':'?', '5':'>', '6':'<',
             '7':';', '8':':', '9':'""',
             '0':'[', ',':']', '.':'{',
             '?':'}', '/':'Ó', '-':'Í',
             '(':'ø', ')':'¶',' ':'€',
             '!':'¬', '@':'»', '#':'³',
             '$':'¡', '%':'½', '*':'^',
             '&':'¿'}

print("""*******Sifreleme Programina Hosgeldiniz********
Artik yazdiklariniz herkes tarafindan okunamayacak.
Sadece siz ve biz...
""")

while True:
    secim = input("1) Sifreleme Yapmak icin 1'e,\n2) Desifreleme icin 2'ye,\n3) Cikmak icin 3'e basiniz.\nSeciminiz:")
    if not secim:
        print("Lutfen giris yapiniz.")
        continue
    elif secim.isdigit() !=True:
        print("Lutfen 1-2-3 rakamlarindan birini giriniz.")
        continue
    else:
        pass
    if secim == "1":
        metin =input("Lutfen sifrelemek istediginiz metni giriniz:")
        sifre = ""
        for harf in metin:
            sifre += sifreleyici[harf]
        print(sifre)
    elif secim == "2":
        metin = input("Lutfen cozmek istediginiz sifrelenmis metni giriniz:")
        desifre = ""
        for karakter in metin:
            desifre += list(sifreleyici.keys())[list(sifreleyici.values()).index(karakter)]
        print(desifre)
    elif secim == "3":
        print("Siz yine de bu sifrelemeye cok guvenmeyin :)\nSistemden Cikiliyor...")
        break

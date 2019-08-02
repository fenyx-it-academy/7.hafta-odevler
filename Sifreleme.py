"""Şifreleme Uygulaması
Kullaniciya iki secenek sunarak orjinal metni sifreli metne ve sifreli metni orjinal metne donusturebilen bir program yazmanizi istiyoruz.
Sozlukler yardimi ile bir sifreleme algoritmasi olusturun ve kullanicidan alacaginiz inputu bu algoritma yoluyla sifreleyin
ve ekrana yazdirin. Kullanici daha sonra bu sifreli metni input olarak yazdiginda orjinal metne ulasabilsin."""
import random
menu="Yapmak istediginiz islemi giriniz:" \
     "1-Sifreleme" \
     "2-Sifre Cozme" \
     "3-Cikis"

karsilik={'a': 'b', 'b': 'e', 'c': 'v', 'd': 'j', 'e': 'Q', 'f': 'w', 'g': 'T', 'h': 'l', 'i': 'O', 'j': 'y', 'k': 'A', 'l': 'W', 'm': 'N', 'n': 'c',
          'o': 'h', 'p': 'F', 'q': 'o', 'r': 'D', 's': 'M', 't': 'C', 'u': 'J', 'x': 'L', 'w': 'Y', 'v': 'I', 'y': 'x', 'z': 'E',
           'A': 'K', 'B': 'X', 'C': 'B', 'D': 'i', 'E': 'R', 'F': 'd', 'G': 'S', 'H': 'H', 'I': 'n', 'J': 'P', 'K': 'f', 'L': 'U', 'M': 's',
          'N': 'r', 'O': 'g', 'P': 't', 'Q': 'Z', 'R': 'G','S': 'm', 'T': 'z', 'U': 'q', 'X': 'V', 'W': 'p', 'V': 'u', 'Y': 'k',' ':'.'}

sifreli=''
rakamlar=[]
sonuc=''
while True:
    print(menu)
    secim=input()
    if secim=="1":
        kelime=input("Sifrelemek istenen kelime:")
        for i in kelime:
            sifreli+=karsilik[i]
        print("sifreli hali:", sifreli)

    elif secim=='2':
        kelime=input("sifresini cozmek istediginiz kelimeyi giriniz:")
        for i in kelime:
            for k,l in karsilik.items():
                if i==l:
                    sonuc+=k
        print("sifrelenen kelime", sonuc)
    elif secim=="3":
        break

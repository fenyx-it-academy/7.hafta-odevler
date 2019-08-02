crypto = {'A': 'X', 'B': 'Y',
          'C': 'Z', 'D': 'A', 'E': 'B',
          'F': 'C', 'G': 'D', 'H': 'E',
          'I': 'F', 'J': 'G', 'K': 'H',
          'L': 'I', 'M': 'J', 'N': 'K',
          'O': 'L', 'P': 'M', 'Q': 'N',
          'R': 'O', 'S': 'P', 'T': 'R',
          'U': 'S', 'V': 'Q', 'W': 'T',
          'X': 'U', 'Y': 'V', 'Z': 'W',
          '=': '*', '+': '**', '*': '/',
          '1': '9', '2': '8', '3': '7',
          '4': '6', '5': '4', '6': '5',
          '7': '3', '8': '2', '9': '1',
          '0': ',', ',': '#', '.': '@',
          '?': '!', '/': ';', '-': '~',
          '(': '+', ')': '-', ' ': '$'}

command = input("""\n'Ceaser ve Binary' sifreleme ve desifreleme modulune 'HOSGELDINIZ...'

- Sifreleme yapmak icin '1' e
- Desifreleme yapmak icin '2' e
- Cikmak icin 'q' giriniz: """).lower()
sifre = ""
desifre = ""

if command == "1":
    kriptola = input("Sifreleyecegin seyi yaz: ").upper()       #upper girilen karakteri tanima uygun yapmak icin
    for item in kriptola:
        sifre += crypto[item]               #her harfin Sifrelemesini yaptiktan sonra bir bosluk eklesinki karismasin
    print(sifre)                                #sifrelemeyi goster
elif command == "2":                            #desifre yapmak icin
    liste = list(crypto.items())
    dekriptola = input("Desifre etmek istediginiz yaziyi giriniz: ").upper()

    for i in dekriptola:                    #sifreli dosya icerisinde tektek geziyoruz
        for j in liste:                     #listeledigimiz sifreli sozluk icerisinde geziyoruz
            if i == j[1]:                   #sifreli dosyadaki eleman sifreli listedeki elemanin 1. elemani ise
                desifre += j[0]             #desifre listesine sifreli sozcuge karsilik gelen karakteri giriyoruz

    print(desifre)

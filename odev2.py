##sifreleme,cozumleme programı##


aciklama="""Bu programla yazdıklarınızı sifreleyebilir,
sifreli yazilari normal haline donusturebilirsiniz.

Yapmak istediginiz islemi giriniz:
      1-sifrele
      2-cozumleme
      3-cikis"""

algoritma={'a': '*', 'b': '.', 'c': '-', 'd': '+',
          'e': '+', 'f': '~', 'g': '//', 'h': '!',
          'i': '3', 'j': '5', 'k': '9', 'l': '%',
          'm': '>', 'n': '_','o': '=', 'p': 'F',
          'q': '.', 'r': 'D', 's': 'M', 't': 'C',
          'u': 'J', 'x': 'é', 'w': '0', 'v': 'I',
          'y': '|', 'z': '<'}

while True:
    try:
        print(aciklama)
        sec=input("Seciminiz: ")
        if not sec:
            print("***Bu bolum bos birakilamaz!!***\n\n")
            continue
        elif sec.isdigit()!=True:
            print(" *** Sadece 1-2-3 rakamlarindan birini seciniz.***\n")
            continue
        else:
            pass

        if sec == "1":
            kelime =input("sifrelencek kelimeyi giriniz: ")
            kelime=kelime.lower()
            if kelime.isalpha()!=True:
                print("***Kelime sadece harf icermelidir!!***")
                continue
            gizli= ""
            for i in kelime:
                gizli += algoritma[i]
            print("Kelimeniz sifrelenmis hali: ",gizli)
        
        elif sec=="2":
            kelime=input("sifresini cozmek istediginiz kelimeyi giriniz:")
            normal=""
            for i in kelime:
                for a,b in algoritma.items():
                    if i==b:
                        normal+=a
            print("Kelimenin normal hali: ", normal)

        elif sec=="3":
            print("Cikiliyor...")
            break
        
    except:
        print("bir hata olustu tekrar deneyiniz!!")


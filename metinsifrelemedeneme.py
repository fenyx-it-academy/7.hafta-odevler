Sozluk = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7',
          'I': '8', 'J': '9', 'K': '10', 'L': '11', 'M': '20', 'N': '40', 'O': '12', 'P': '21', 'Q': '39',
          'R': '13', 'S': '22', 'T': '38', 'U': '14', 'V': '23', 'W': '37', 'X': '15', 'Y': '24', 'Z': '36',
          '1': '16', '2': '25', '3': '35', '4': '17', '5': '26', '6': '34', '7': '18', '8': '27', '9': '33',
          '0': '19', ', ': '28', '.': '32', '?': '41', '/': '29', '-': '31', '(': '42', ')': '30'}

print("""
	      =============================================="
	      |                                            |
	      |             METIN SIFRELEME                |
	      |                PROGRAMI                    |
	      |                 V 1.0                      |
	      ==============================================\n\n""")
while True:
    secim = input("""Metin Sifrelemek icin       1'e
	Metin Desifreleme icin de   2'ye basiniz : """)

    if secim == "1":
        metin = input("Lutfen  metni giriniz:\n").upper()
        sifrelenen = ""
        for i in metin:
            if i != " ":
                sifrelenen += Sozluk[i] + " "
            else:
                sifrelenen += " "
        print(sifrelenen)

    if secim == "2":
        metin = input("Lutfen  metni giriniz:\n")
        metin += " "
        cozulen = ""
        sifre_kar = ""

        for harf in metin:
            if harf != " ":
                i = 0
                sifre_kar += harf
            else:
                i += 1
                if i == 2:
                    cozulen += " "
                else:
                    cozulen += list(Sozluk.keys())[list(Sozluk.values()).index(sifre_kar)]
                    sifre_kar = ""

        print(cozulen)
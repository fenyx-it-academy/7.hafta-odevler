key = 'abcdefghijklmnopqrstuvwxyz'
text = input("Sifrelenecek metni giriniz: ")
offset = 5

while True:
    print(" 1-orjinal metni sifreli metne donustur\n 2-sifreli metni orjinal metne donustur\n 3-çıkış")
    secim = input("\t\t\tyapacaginiz islemi seciniz: ")

    if (secim == "1"):
        n = offset
        plaintext = text
        result = ''

        for l in plaintext.lower():
            try:
                i = (key.index(l) + n) % 26
                result += key[i]
            except ValueError:
                result += l
        encrypted = result.lower()
        print(result.lower())

    if (secim == "2"):
        try:
            n = offset
            ciphertext = encrypted
            result = ''

            for l in ciphertext:
                try:
                    i = (key.index(l) - n) % 26
                    result += key[i]
                except ValueError:
                    result += l
            print(result)
        except:
            print("İlk önce şifreleme yapmak zorundasınız")

    if (secim == "3"):
        print("Çıkış yapılıyor")
        break

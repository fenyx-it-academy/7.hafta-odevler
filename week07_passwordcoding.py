import time
print('Simple Encryption, Please Choose A Transaction')

coding = {




"A":"K",
"a":"k",
"B":"I",
"b":"i",
"C":"P",
"c":"p",
"Ç":"R",
"ç":"r",
"D":"H",
"d":"h",
"E":"İ",
"e":"İ",
"F":"G",
"f":"g",
"G":"F",
"g":"f",
"Ğ":"Ö",
"ğ":"ö",
"H":"D",
"h":"d",
"I":"B",
"i":"b",
"İ":"E",
"İ":"e",
"J":"S",
"j":"s",
"K":"A",
"k":"a",
"L":"Q",
"l":"q",
"M":"Y",
"m":"y",
"N":"U",
"n":"u",
"O":"N",
"o":"n",
"Ö":"T",
"ö":"t",
"P":"M",
"p":"m",
"Q":"L",
"q":"l",
"R":"Z",
"r":"z",
"S":"J",
"s":"j",
"Ş":"W",
"ş":"w",
"T":"X",
"t":"x",
"U":"V",
"u":"v",
"Ü":"Ç",
"ü":"ç",
"V":"O",
"v":"o",
"W":"Ş",
"w":"ş",
"X":"Ğ",
"x":"ğ",
"Y":"C",
"y":"c",
"Z":"Ü",
"z":"ü",
"1":"7",
"2":"8",
"3":"9",
"4":"0",
"5":"1",
"6":"2",
"7":"3",
"8":"4",
"9":"5",
"0":"6",
".":",",
",":".",
"?":">",
" ":"*",


}
while True:
    sel = input("-»Transaction«-\n"
                 "Encryption    --»1\n"
                 "Decryption    --»2\n"
                 "Exit          --»0\n")


    if sel == "1":
        text_encrypted = ""
        text = input("Pls type your text here:\n")
        for i in text:
            text_encrypted += coding[i]
        print("""\nThe text encrypted as\n " {} "\n """.format(text_encrypted))

    elif sel == "2":
        text_decrypted = ""
        list2 = list(coding.items())

        text_encrypted = input("Pls type your text here:\n")
        for a in text_encrypted:
            for b in list2:
                if a == b[1]:
                    text_decrypted += b[0]
        print("""\n The text decryted as" {} "\n""".format(text_decrypted))

    elif sel == "0":
        print("Görüşmek üzere, prg sonladırılıyor!!")
        time.sleep(1)
        quit()
    else:
        print("'Pls type 1 or 2 or to exit 0'\n")
        continue
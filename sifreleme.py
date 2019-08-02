alfabe="abcdefghijklmnopqrstuxvwyz., "
alfabe=list(alfabe)
deger=alfabe[::-1]
sifreleme={}
for i in range(len(alfabe)):
    sifreleme[alfabe[i]]=deger[i]

metin=input("sifrelemek veya cozmek istediginiz metni giriniz:")
yeni_metin=[]
for i in list(metin):
    yeni_metin.append(sifreleme[i])
    yenimet="".join(yeni_metin)
print(yenimet)
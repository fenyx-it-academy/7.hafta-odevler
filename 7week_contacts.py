'''telefon rehberi uygulamasi
Bu odevde bir telefon rehberi simulasyonu yapmanizi istiyoruz.
Program acildiginda kullaniciya, rehbere kisi ekleme, kisi silme, kisi isim ya da tel bilgisi guncelleme,
rehberi listeleme seceneklerini sunun. Kullanicinin secimine gore gerekli inputlarla programinizi sekillendirin.
Olusturulan rehberi bir dosyaya kaydedin.
Rehberi olustururken sozlukleri kullanin.'''
print("Welcome to the phone contacts programme!")
print("Choose one of the subjects:\n"
      "1) add contacts\n"
      "2) delete contacts\n"
      "3) Update existing contacts\n"
      "4) list contacts\n"
      "5) Quit")
#we are giving information to user about contacts programme
contacts={"Steven Gerrard":"0507", "Michael Owen":"0505", "Ronaldo Nazario":"0733264"}
updated={}
turning_point=True
#we are making a loop till working user make value of "turning point" false
while turning_point:
    choice = int(input("Make your choice:"))
    if choice == 1: #adding new contact
        ky = input("Contact Name:")
        val = input("Contact nummer:")
        contacts[ky] = val
        print(contacts)
        continue
    elif choice == 2:  #deleting existing contact
        print(contacts)
        deleted=input("Please enter name of you want to delete contact:")
        print(contacts.pop(deleted,"please make sure you are deleting the existing contact or the contact not found."))
        continue
    elif choice == 3:  #updating contacts
        print("Give information about contacts you want to update:")
        ky = input("Contact Name:")
        val = input("Contact nummer:")
        updated[ky] = val
        contacts.update(updated)
        print(contacts)
        continue
    elif choice == 4:  #listing contacts
        print(list(contacts))
    elif choice == 5:  #Exiting the program.
        print("Exiting the contacts...")
        turning_point=False
#newcontacts=(burasi eksik) dosyaya yazdirmak nasil oluyor sozluklerde calismayan bir ozellik
#with open("contacts.txt","w+",encoding="utf-8")as file:  #contacts degerini sozlukten baska bir degere cevirmeliyiz.
    #file.write(list(contacts))
   # print(file)


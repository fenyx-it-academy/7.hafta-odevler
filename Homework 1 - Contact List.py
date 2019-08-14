print("********** Contact List **********\n\n\n")
contact_list={}
while True:
    operation=input("""This is a contact list program.
Please choose a operation you would like to do;
To add a contact, press            "1"
To delete a contact, press         "2"
To update the contact list, press  "3"
To list the contact list, press    "4"
To exit the program, press         "e"
""")
    if operation == "1":
        name=input("Please enter name and surname you would like to add.\n").lower()
        key=0
        while key==0:
         number=input("Please enter phone number you would like to add.\n")
         if number.isdigit():
          if contact_list=={}:
            contact_list[name]=number
            key=1
            print("New contact has been successfully added.")
            print("Your contact list is: ",contact_list,"\n")
          else:
            for k,v in contact_list.items():
                if k==name and v==number:
                    print("The contact is already in the contact list. Please check the information!!!")
                    key=1
                else:
                    contact_list[name]=number
                    print("New contact has been successfully added.")
                    print("Your contact list is: ",contact_list,"\n")
                    key=1
                    break
         else:
            print("Phone number must consists of only numbers!!!. Please check.")
            x=0
            while x==0:
                q=input("To continue the addition, please press: 'ENTER'\nTo exit the addition, please press: 'q'\nTo exit the program, please press:'e'\n")
                if not q:
                    x=1
                    continue
                elif q.lower()=="q":
                    print("Addition operation terminated!!!\n")
                    x=1
                    key=1
                elif q.lower()=="e":
                    print("Program terminated!!!\n")
                    exit()
                else:
                    print("You entered an incorrect code. Please check and read instructions!!!\n")
                    continue
        continue
    elif operation == "2":
        print("Your contact list is: ",contact_list,"\n")
        x=0
        while x==0:
         name=input("Please enter name and surname you would like to delete.\n").lower()
         for i in contact_list.keys():
            if i == name:
                contact_list.pop(name)
                print("The name you entered has been successfully deleted.")
                print(contact_list)
                x=1
                break
            else:
                print("The name you entered is not in the contact list. Please check the information!!!\n")
                key=0
                while key==0:
                 q=input("To continue the deletion, please press: 'ENTER'\nTo exit the deletion, please press: 'q'\nTo exit the program, please press:'e'\n")
                 if not q:
                    key=1
                    break
                 elif q.lower()=="q":
                    print("Deletion operation terminated!!!\n")
                    key=1
                    x=1
                    break
                 elif q.lower()=="e":
                    print("Program terminated!!!\n")
                    exit()
                 else:
                    print("You entered an incorrect code. Please check and read instructions!!!\n")
                    continue
    elif operation == "3":
     while True:
      new=input("To update name and surname, please press '1'\nTo update phone number, please press   '2'\nTo exit the updating, please press: 'q'\nTo exit the program, please press:'e'\n")
      try:
        if new.lower()=="q":
            print("Updating operation terminated!!!\n")
            break
        elif new.lower()=="e":
            print("Program terminated!!!\n")
            exit()
        elif new == "1":
            print("Your contact list is: ",contact_list,"\n")
            name=input("Please enter name and surname you would like to update.\n").lower()
            new_name=input("Please enter updated name and surname.\n").lower()
            contact_list[new_name] = contact_list.pop(name)
            print("The contact list has been successfully updated.")
            print("Your updated contact list is:",contact_list,"\n")
            continue
        elif new=="2":
            print("Your contact list is: ",contact_list,"\n")
            name=input("Please enter name and surname you would like to update.\n").lower()
            for i in contact_list.keys():
                if i == name:
                    new_number=input("Please enter updated phone number.\n")
                    contact_list[name]=new_number
                    print("The contact list has been successfully updated.")
                    print("Your updated contact list is:",contact_list,"\n")
                    break
                else:
                    print("The contact name and surname is not in contact list. Please check!!!")
            continue
        else:
            print("You made an incorrect code. Please check and read instructions!!!\n")
            continue
      except KeyError:
         print("The contact name and surname is not in contact list. Please check!!!")
         continue
    elif operation=="4":
        for k,v in contact_list.items():
            print(f'{k}:{v}.\n')
    elif operation.lower() == "e":
        print("Program terminated.")
        break
    else:
        print("You made an incorrect code. Please check and read instructions!!!\n")
with open("Contact List.txt", "a") as contact:
    for k,v in contact_list.items():
        contact.write(f'{k}:{v}.\n')

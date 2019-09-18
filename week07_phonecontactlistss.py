contact1={}
contact2={}
file_contact=open("telephonecontacts.txt", "r" )

file_contact.seek(0)

r1=file_contact.read()
full_list=r1.split("___")


#######################################################################################
for i in full_list:
    if full_list.index(i)%2==0:
        name=i
    else:
        number=i
        contact1[name]=number
        contact2[number]=name
file_contact.close()

#######################################################################################

print("Welcome To Telephone Book Trials")
contact1={}
contact2={}
contact_count=0
a=1
while a==1:

    sel=input("\n_Please choose your transaction_\n"
              "*Add new contact     --» 1\n"
              "*Browse contacts     --» 2\n"
              "*Update contact Name --» 3\n"
              "*Update contact No   --» 4\n"
              "*Save&Exit           --» q*\n")
    if sel=="1" or sel=="2" or sel=="3" or sel=="4" or sel =="5":

#######################################################################################
        if sel=="1":
            name=input("Please enter your contact name:")
            number=input("Please enter your contact's number")
            contact1[name]=number
            contact2[number]=name
            print("\"",contact2[number],"--",contact1[name],"\"","has been saved")
            continue
#######################################################################################
        if sel=="2":
                for i in contact1:
                    print("{:25}... {}".format(i,contact1[i]))

        elif sel=="Q" or sel =="q":
            break

#######################################################################################
        if sel=="3":
            name = input("Please enter name for update")
            if name not in contact1:
                print("Sorry there is number name in contacts")
                continue
            else:
                new_name = input("Please enter new name")
                number_spare = contact1[name]
                contact2[number_spare] = new_name
                contact1[new_name] = contact1.pop(name)
#######################################################################################
        if sel=="4":
                print(contact2)
                number = input("Please enter number for update")

                if number not in contact2:
                    print("Sorry there is number number in contacts")
                    continue
                else:
                    new_number=input("Please enter new number")
                    name_spare=contact2[number]
                    contact1[name_spare]=new_number
                    contact2[new_number]=contact2.pop(number)

#######################################################################################
    else:
            print("Please press one of the given sections")
filecontact=open("telephonecontacts.txt", "w" )
for i in contact1:
    save=i+"___"+contact1[i]+"___"
    file_contact.write(save)

file_contact.close()
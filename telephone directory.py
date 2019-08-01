print ("*****TELEPHONE DIRECTORY***")
database={}
update={}

while True:
    choice=input('''Pls enter your choice
1.Add a contact
2.Delete a contact
3.Edit a contact
4.List your Contacts''')

while True:
    if choice=="1":
       name=input("Enter the name")
       number=input("Enter the number: ")
       database[name]=number
       print(database)

        
    if choice=="2":
        choice= input("Enter the contact you want to delete:")
        database.pop(choice)       
        print(database)
        
    if choice=="3":
        secim3 = input("Select the contact you want to delete : ")
        print("Number : ",database[choice3])
        database.pop(choice3)      
        name = input("Name : ")
        number = input("number : ")
        update[name]=number
        database.update(update)      
        print(veritabani)
        
    if choice=="4":
           if databese!="":
               print(database)
              
           
        
           

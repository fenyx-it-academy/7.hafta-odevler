print("*"*15,"TELEPHONE DIRECTORY","*"*15)
print("""
Welcome to Telephore Directory
Please choose the options below:
-Press 1 to add somebody's number in telephone directory 
-Press 2 to delete somebody's number from telephone directory
-Press 3 to update somebody's number
-Press 4 to see all numbers
-Press s to save and quit from telephone directory""")

directory={}
try:
    while True:
        replying = input("Plese enter your procees which you want:")
        
        if replying == "1":
            name = input("What is the name and surname of person which you want to add in telephone directory:")
            if name.isdigit() == True:                                                  #check the name consist of letter
                print("This section for names,please enter letter\n")
                continue
            number = input("What is the number of person which you want to add in telephone directory:")
            if number.isalpha() == True:                                                #check the number consist of digit
                print("This section for numbers,please enter digit\n")
                continue
            elif name in directory.keys():                                              #check whether name is in 'directory' dictionary 
                answer = input(f"{name} is already exist.Do you want to change it?(y/n)")#if user still add the name
                if answer.lower == "y":                                             
                    directory[name] = number
                elif answer.lower == "n":
                    print(f"{name} will not add to telephone directory\n")
                    continue
                else:
                    print("your enter is wrong,please try again\n")
            else:
                directory[name] = number                                                #if there is no proble,register the name and number
                print(f"{name} have been added\n")
                
        elif replying == "2":
            name = input("What is the name and surname of person which you want to delete from telephone directory:")
            if name not in directory.keys():                                            #check name is already exist
                print("This name is not exist,please try again\n")
                continue
            else:
                delete_name = directory.pop(name)   
                print(f"{name} have been deleted")
            
        elif replying == "3":
            answer = input("If you want to update person press p, if you want to update number press n:")
            if answer.lower() == "p":
                update_name = input("Which name do you want to update:")                #the existing name in order to change it
                if update_name not in directory.keys():                                 #check  update name is already exist
                    print("This name is not in telephone directory,please try again\n")
                    continue
                new_name = input("What is the new name:")                               #new name to update
                if new_name.isdigit() == True:
                    print("This section for names,please enter letter\n")
                    continue
                value_update_name = directory.pop(update_name)                          #delete name which in dictioanary and set its value in variable'value_update_name'
                directory[new_name] = value_update_name                                 #add the new name into the dictonary and add the variable'value_update_name' as its value
                print("your update have been applied\n")
            elif answer.lower() == "n":
                update_name = input("Which name's number do you want to update:")       ##the existing name in order to change its number
                if update_name not in directory.keys():
                    print("This name is not in telephone directory,please try again\n")
                    continue
                new_number = input("What is the new number:")
                if new_number.isalpha() == True:
                    print("This section for numbers,please enter digit\n")
                    continue
                directory[update_name] = new_number                                     #change its keys
                print("your update have been applied\n")
            else:
                print("You should enter p or n,please tyr again\n")
                continue
                
        elif replying == "4":
            for key, value in directory.items():                                        #use for loop in order to take dictionary's key and value
                print(f"{key} : {value}\n")
            if directory == {}:
                print("There is no registry to show\n")
                
        elif replying == "s":
            break

        else:
            print("please enter options above\n")

        
    with open("directory.txt","w") as file:
        for name,number in directory.items():
            file.write(f"{name.ljust(15)}:{number}\n")
except (ValueError,KeyError):
    print("your enter is wrong, please try again\n")
except:
    print("something happened wrong, please try again\n")

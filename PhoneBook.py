import time
message = """ 
Please select an action from the following menu
{}
1-Add a person to the phone book
2-Delete a person from the phone book
3-Update a name or a number
4-Show the phone book
Press q to quit: """

phoneBook = {}
action = ''
while str(action).lower() != 'q':
    try:
        action = input(message.format('-'*47))
        if action == '1':
            name = input("\nEnter the full name of the person you want to add to the phone book:\n").lower().title()
            if name not in phoneBook:
                telNumber = input("Enter the phone number of the person you want to add to the phone book:\n")
                phoneBook.setdefault(name, telNumber)
                print('\nContact is being added....')
                time.sleep(1)
                print('\nYour phone book is updated.')
            else:
                print("\nThis person already exists in your phone book!"
                      "\nIf you'd like to change this person's phone number, select 3 from the menu. ")
        elif action == '2':
            name = input("\nEnter the full name of the person "
                         "you want to delete from the phone book:\n").lower().title()
            print('\nSearching for the name {} in your phone book...'.format(name))
            time.sleep(1)

            if name not in phoneBook:
                print('\nThe person you want to delete is not in your phone book!\n')
            else:
                print('\nContact is being deleted....')
                time.sleep(1)
                phoneBook.pop(name)
                print('\nYour phone book is updated.')
        elif action == '3':
            name = input("\nEnter the full name of the person whose information "
                         "you want to update from the phone book:\n").lower().title()
            print('\nSearching for the name {} in your phone book...'.format(name))
            time.sleep(1)
            if name not in phoneBook:
                print('\nThe person whose information you want to update is not in your phone book!\n')
            else:
                update_item = input('\nDo you wish to update a name or a phone number? '
                                    "\nPlease enter 'n' for 'name' and 'p' for 'phone number': ").lower()
                if update_item == 'n':
                    new_name = input("\nEnter the new name to update: ").lower().title()
                    phoneBook[new_name] = phoneBook[name]
                    phoneBook.pop(name)
                elif update_item == 'p':
                    new_phone_no = input("\nEnter the new phone number to update: ")
                    phoneBook[name] = new_phone_no
                else:
                    print('\nYou have made a wrong entry!')
                print('\nContact information is being updated....')
                time.sleep(1)
                print('\nYour phone book is updated.')
        elif action == '4':
            print('\nFetching phone book information...\n\n')
            time.sleep(1)
            print('\n' + 'YOUR PHONE BOOK'.center(40) + '\n\n' + 'Name'.center(20) +
                  'Phone No'.center(20) + '\n' + '='*20 + '='*20)
            for k,v in phoneBook.items():
                print(f'{k}'.center(20) + '|' + f'{v}'.center(20) +
                      '\n' + '-' * 20 + '-' * 20)
            if phoneBook == {}:
                print("\nYou don't have any contacts in your phone book yet. "
                      "\nPlease select '1' from the main menu if you wish to add contacts.")
            print('\n\n')
        else:
            raise ValueError
    except ValueError:
        print('You have made a wrong entry\n')

with open('Phone Book.txt', 'w', encoding='utf-8') as phone_book:
    phone_book.write('Name'.center(20) + 'Phone No'.center(20) +
                     '\n' + '='*20 + '='*20 + '\n')
    for k,v in phoneBook.items():
        phone_book.write(f'{k}'.lower().title().center(20) + '|' + f'{v}'.lower().title().center(20) +
                         '\n' + '-' * 20 + '-' * 20 + '\n')
    phone_book.flush()
import os
from contact import Contact
from phonebook import PhoneBook

main_instructions: str = """commands:
        /Help - show hints
        /Show - show contacts page by page
        /Add - add new contact
        /Edit - edit contact chose from 
        /Search - looking for contact
        /Save - to save changes to file
        /Exit - exit from program
"""

def mainLoop():
    """main loop

    No arguments
    No returned value
    Infinitly print hints, how you can work with it. And ask to input command

    """
    while True:
        print(main_instructions)
        cmd: str = input('Enter the command:\n')
        match cmd:
            case '/Help':
                continue
            case '/Show':
                PhoneBook.showMenu()
            case '/Add':
                if not os.access('phonebook.json', os.W_OK):
                    print('Error: file have no access to write')
                else:
                    PhoneBook.addNewContact()
            case '/Edit':
                if not os.access('phonebook.json', os.W_OK):
                    print('Error: file have no access to write')
                else:
                    PhoneBook.editContact()
            case '/Save':
                PhoneBook.writeToFile()
            case '/Search':
                PhoneBook.searchContact()
            case '/Exit':
                PhoneBook.safeExit()
            case _:
                sepCmd: list = cmd.split(' ')
                if (len(sepCmd) == 2 and sepCmd[0] == '/Edit' and sepCmd[1].isdigit):
                    PhoneBook.editContact(int(sepCmd[1]))
                print('unknow command.')

def main():
    """main function.
    
    No arguments
    No returned value
    
    Check exists file, if not -> create it
    Check rights on read of file, if not -> print error + exit
    Get all data from file
    Launch main loop
    
    """
    if not os.access('phonebook.json', os.F_OK):
        file: file = open('phonebook.json', 'w+')
        file.write([])
        file.close
    elif not os.access('phonebook.json', os.R_OK):
        print('Error: file have no access to read')
        exit()
    PhoneBook.getFromFile()
    mainLoop()

if __name__ == "__main__":
    main()
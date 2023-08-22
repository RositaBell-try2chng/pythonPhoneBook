import os
from contact import Contact
from phonebook import PhoneBook


main_instructions: str = """commands:
/Help - show hints
/Show - show contacts page by page
/Add - add new contact
/Edit - edit contact
/Search - looking for contact
/Exit - exit from program
"""

def mainLoop(phb: PhoneBook):
    while True:
        cmd = input('Enter the command:\n')
        match cmd:
            case '/Help':
                print(main_instructions)
            case '/Show':
                phb.showMenu()
            case '/Add':
                if not os.access('phonebook.json', os.W_OK):
                    print('Error: file have no access to write')
                else:
                    phb.addNewContact()
            case '/Edit':
                if not os.access('phonebook.json', os.W_OK):
                    print('Error: file have no access to write')
                else:
                    None #edit contact
            case '/Search':
                None #Search
            case '/Exit':
                exit()
            case _:
                print('unknow command. To help use /Help')
def main():
    if not os.access('phonebook.json', os.F_OK):
        file = open('phonebook.json', 'w+')
        file.write([])
        file.close
    elif not os.access('phonebook.json', os.R_OK):
        print('Error: file have no access to read')
    phb: PhoneBook = PhoneBook()
    print(main_instructions)
    mainLoop(phb)

if __name__ == "__main__":
    main()
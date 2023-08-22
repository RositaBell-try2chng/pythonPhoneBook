from contact import Contact
import json
import shutil

input_hints: list = ['input first Name: ', 'input last Name: ']

class PhoneBook:
    phb: dict = {}
    nextId: int = 1

    def __init__(self):
        try:
            with open('phonebook.json', 'r') as file:
                contacts_array = json.load(file)
                for one in contacts_array:
                    contactToInsert: Contact = Contact()
                    contactToInsert.setFirstName(one.get('first_name'))
                    PhoneBook.phb[one['id']] = contactToInsert
                    PhoneBook.nextId += 1
                # file.close()
        except:
            print('EXCEPTION:\nsomething wrong with file')
            exit()
            
    @staticmethod
    def printShort(pageNo: int):
        offset: int = (pageNo - 1) * 9
        for i in range(9):
            if (PhoneBook.phb.get(i + offset) is not None):
                print(i + offset, end = ' ')
                PhoneBook.phb[i + offset].printContact()

    def addNewContact(self):
        tmp: Contact = Contact()
        id: int = PhoneBook.nextId
        attr: list = []
        PhoneBook.nextId += 1
        for hint in input_hints:
            nextAttr: str = input(hint)
            if len(nextAttr) == 0:
                attr.append(None)
            else:
                attr.append(nextAttr)
        tmp.fillFields(attr)
        PhoneBook.phb[id] = tmp
        self.writeToFile()


    def makeBackup(self):
        try:
            src = open('phonebook.json', 'r')
            dst = open('phonebook_backup.json', 'w+')
            shutil.copyfileobj(src, dst)
        except:
            print('cannot make backup, so we dont change file. Contact have not been added. Exit from Program')
            exit()

    def restoreFromBackup(self):
        try:
            dst = open('phonebook.json', 'w+')
            src = open('phonebook_backup.json', 'r')
            shutil.copyfileobj(src, dst)
        except:
            print('cannot restore file from backup. exit from Program')
            exit()
        


    def writeToFile(self):
        self.makeBackup()
        try:
            toDump: list = []
            for one in PhoneBook.phb:
                tmpToDump: json = {
                    "id": one,
                    "first_name": PhoneBook.phb[one].getFirstName()
                }
                toDump.append(tmpToDump)
            with open('phonebook.json', 'w') as file:
                json.dump(toDump, file)
        except:
            self.restoreFromBackup()

    @staticmethod
    def showMenuHints(currentPage: int, pgs: float):
        if (currentPage < pgs):
            print('Enter /Next to show next Page')
        if (currentPage > 1):
            print('Enter /Previous to show previous Page')
        print('Enter /Inspect <id>, to inspect concrete contact')
        print('Enter /Back to return to main menu')

    @staticmethod
    def showMenu() -> None:
        if (len(PhoneBook.phb) == 0):
            print('Have no contacts, return to main menu')
            return
        currentPage: int = 1
        pgs: float = ((PhoneBook.nextId - 1) / 2)
        print(f'Page {currentPage}:')
        PhoneBook.printShort(currentPage)
        while True:
            PhoneBook.showMenuHints(currentPage, pgs)
            showCommand: str = input()
            match showCommand:
                case '/Back':
                    print('Return to main menu\n')
                    return
                case '/Next':
                    if (currentPage >= pgs):
                        print('ERROR: wrong command\n')
                    else:
                        currentPage += 1
                        PhoneBook.printShort(currentPage)
                        print()
                case '/Previous':
                    if (currentPage <= 1):
                        print('ERROR: wrong command\n')
                    else:
                        currentPage -= 1
                        PhoneBook.printShort(currentPage)
                        print()
                case '':
                    print('ERROR: no command\n')
                case _:
                    cmdSplit: list = showCommand.split(' ')
                    if (cmdSplit[0] == '/Inspect' and len(cmdSplit) == 2 and cmdSplit[1].isdigit()):
                        id: int = int(cmdSplit[1])
                        if (PhoneBook.phb.get(id) is not None):
                            print(f'Contact with id = {id}:')
                            PhoneBook.phb[id].inspectContact()
                            print()
                        else:
                            print(f'Not found contact with id = {id}\n')
                    else:
                        print('ERROR: wrong command\n')


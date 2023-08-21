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
            

    def printShort(self):
        for one in PhoneBook.phb:
            print(one, end = ' ')
            PhoneBook.phb[one].printContact()

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


from contact import Contact
import json
import shutil

class PhoneBook:
    phb: dict = {}
    nextId: int = 1
    flgChng: bool = False

    @staticmethod
    def getFromFile():
        try:
            with open('phonebook.json', 'r') as file:
                contactsList: list = json.load(file)
                for one in contactsList:
                    contactToInsert: Contact = Contact()
                    contAttrs: dict = contactToInsert.getAttrs()
                    for at in contAttrs:
                        contactToInsert.setAttr(at, one.get(at))
                    PhoneBook.phb[one['id']] = contactToInsert
                    PhoneBook.nextId += 1
                file.close()
        except:
            print('EXCEPTION:\nsomething wrong with file')
            exit()
            
    @staticmethod
    def countIdLen(pageNo: int) -> int:
        maxIdOnPage: int = pageNo * 9
        res: int = 1
        while maxIdOnPage >= 10:
            res += 1
            maxIdOnPage /= 10
        return res

    @staticmethod
    def printHat(pageNo: int):
        idLen: int = PhoneBook.countIdLen(pageNo)
        if idLen < 2:
            idLen = 2
        string: str = '+'
        for i in range(idLen):
            string += '-'
        string += '+'
        string += '----------+' * 6
        string2: str = '|' + (' ' * (idLen - 2)) + 'id' + '|'
        string2 += 'first name|last name |mid. name |org. name |work phone|per. phone|'
        print(string + '\n' + string2 + '\n' + string)
        
    @staticmethod
    def printShort(pageNo: int):
        offset: int = (pageNo - 1) * 9
        PhoneBook.printHat(pageNo)        
        for i in range(9):
            if (PhoneBook.phb.get(i + offset) is not None):
                print('|', end = '')
                if (i + offset) / 10 < 1:
                    print(i + offset, end = ' ')
                else:
                    print(i + offset, end = '')
                PhoneBook.phb[i + offset].printContact()

    @staticmethod
    def addNewContact():
        tmp: Contact = Contact()
        id: int = PhoneBook.nextId
        attrs: dict = tmp.getAttrs()
        PhoneBook.nextId += 1
        for at in attrs:
            value: str = input(f'set {at}: ')
            tmp.setAttr(at, value)
        PhoneBook.phb[id] = tmp
        PhoneBook.writeToFile()

    @staticmethod
    def makeBackup() -> int:
        try:
            src: file = open('phonebook.json', 'r')
            dst: file = open('phonebook_backup.json', 'w+')
            shutil.copyfileobj(src, dst)
            return 1
        except:
            return 0

    @staticmethod
    def restoreFromBackup():
        try:
            dst: file = open('phonebook.json', 'w+')
            src: file = open('phonebook_backup.json', 'r')
            shutil.copyfileobj(src, dst)
        except:
            print('cannot restore file from backup. exit from Program')
            exit()
        
    @staticmethod
    def getJsonToInsert(one: int) -> json:
        res: json = {"id": one}
        res.update(PhoneBook.phb.get(one).getAttrs())
        return res

    @staticmethod
    def writeToFile():
        if PhoneBook.makeBackup() == 1:
            try:
                toDump: list = []
                for one in PhoneBook.phb:
                    tmpToDump: json = PhoneBook.getJsonToInsert(one)
                    toDump.append(tmpToDump)
                with open('phonebook.json', 'w') as file:
                    json.dump(toDump, file)
                PhoneBook.flgChng = False
                print('The file was overwritten successfully')
            except:
                print('trying to dump failed, restore file from backup')
                PhoneBook.restoreFromBackup()
        else:
            print('ERROR: cannot make backup, so we dont save changes in file.')
    
    def inspectMenuHints():
        hints: str = """Inspect Menu Commands:
        /Back - return to Show menu
        /Exit - Exit from program
        /Edit - open Edit menu
        /Save - Save changes
        /Repeat - show all about contact again"""
        print(hints)

    @staticmethod
    def inspectMenu(id: int):
        print(f'Now you are in /Inspect menu!')
        print(f'Contact with id = {id}:')
        PhoneBook.phb[id].inspectContact()
        print()
        while True:
            PhoneBook.inspectMenuHints()
            inspectCommand = input()
            match inspectCommand:
                case '/Back':
                    print('return to Show menu')
                    return
                case '/Exit':
                    PhoneBook.safeExit()
                case '/Save':
                    PhoneBook.writeToFile()
                case '/Edit':
                    PhoneBook.editContact(id)
                    continue
                case '/Repeat':
                    print(f'Contact with id = {id}:')
                    PhoneBook.phb[id].inspectContact()
                case _:
                    print('unknown command')

    @staticmethod
    def showMenuHints(currentPage: int, pgs: float):
        hints: str = 'show menu commands:\n'
        if (currentPage < pgs):
            hints += '        /Next - to show next Page\n'
        if (currentPage > 1):
            hints += '        /Previous - to show previous Page'
        hints += '''        /Show - show current Page
        /Edit <id> - to change contact
        /Inspect <id> - to inspect concrete contact and edit if you want
        /Add - to add new contact
        /Back - to return to main menu
        /Exit - to exit from program'''
        print(hints)

    @staticmethod
    def showMenu() -> None:
        print('Now you are in /Show menu!')
        if (len(PhoneBook.phb) == 0):
            print('Have no contacts, return to main menu')
            return
        currentPage: int = 1
        print(f'Page {currentPage}:')
        PhoneBook.printShort(currentPage)
        while True:
            pgs: float = ((PhoneBook.nextId - 1) / 9)
            PhoneBook.showMenuHints(currentPage, pgs)
            showCommand: str = input()
            match showCommand:
                case '/Back':
                    print('Return to main menu\n')
                    return
                case '/Exit':
                    PhoneBook.safeExit()
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
                case '/Search':
                    PhoneBook.searchContact()
                case '/Show':
                    print(f'Page {currentPage}:')
                    PhoneBook.printShort(currentPage)
                case '/Add':
                    PhoneBook.addNewContact()
                case '/Save':
                    PhoneBook.writeToFile()
                case '':
                    print('ERROR: no command\n')
                case _:
                    cmdSplit: list = showCommand.split(' ')
                    if (cmdSplit[0] == '/Inspect' and len(cmdSplit) == 2 and cmdSplit[1].isdigit()):
                        id: int = int(cmdSplit[1])
                        if (PhoneBook.phb.get(id) is not None):
                            PhoneBook.inspectMenu(id)
                        else:
                            print(f'Not found contact with id = {id}\n')
                    elif (cmdSplit[0] == '/Edit' and len(cmdSplit) == 2 and cmdSplit[1].isdigit()):
                        id: int = int(cmdSplit[1])
                        if (PhoneBook.phb.get(id) is not None):
                            PhoneBook.editContact(id)
                        else:
                            print(f'Not found contact with id = {id}\n')
                    else:
                        print('ERROR: wrong command\n')
    

    @staticmethod
    def editContact(id: int = 0):
        if id == 0:
            print("You should chose contact in /Show -> /Inspect <id> -> /Edit to edit contact")
            PhoneBook.showMenu()
            return
        cont: Contact = PhoneBook.phb.get(id)
        if (cont is None):
            print(f'Contact with id = {id} not found, return to previous menu')
            return
        print('Edit menu for contact:')
        cont.inspectContact()
        contactsParams: dict = cont.getAttrs()
        for param in contactsParams:
            value = input(f'''Do you want to change {param}?
            \b<Empty> - to skip
            \b/Clean- to set value as None
            \b/End - to finish
            \bWhatever else to set new value\n''')
            match value:
                case '/End':
                    return
                case '':
                    continue
                case '/Clean':
                    PhoneBook.flgChng = True
                    cont.setAttr(param, None)
                case _:
                    PhoneBook.flgChng = True
                    cont.setAttr(param, value)
    
    @staticmethod
    def checkEqual(who: Contact, tmp: Contact) -> bool:
        for at in tmp.getAttrs():
            atTmp: str = tmp.getAttr(at)
            atWho: str = who.getAttr(at)
            if (atTmp is not None and (atWho is None or (atWho is not None and atTmp not in atWho))):
                return False
        return True

    @staticmethod
    def getAllBy(tmp: Contact) -> dict:
        res: dict = {}
        for one in PhoneBook.phb:
            if (PhoneBook.checkEqual(PhoneBook.phb.get(one), tmp)):
                res[one] = PhoneBook.phb.get(one)
        return res

    @staticmethod
    def searchContact():
        flg: bool = False
        res: dict = {}
        tmpCont: Contact = Contact()
        contactsParams: dict = tmpCont.getAttrs()
        for param in contactsParams:
            value = input(f'''Do you want to set {param} for search?
            \b<empty> - to skip
            \b/Start - end input params and start to search
            \bWhatever else to set new value in this param for search\n''')
            match value:
                case '':
                    continue
                case '/Start':
                    res = PhoneBook.getAllBy(tmpCont)
                    flg = True
                    break
                case _:
                    tmpCont.setAttr(param, value)
        if (not flg):
            res = PhoneBook.getAllBy(tmpCont)
            flg = True
        print(f'{len(res)} results have been found')
        for one in res:
            print(f'{one} -> ', end = '')
            res[one].printContact()
    
    @staticmethod
    def safeExit():
        if not PhoneBook.flgChng:
            exit()
        res: str = input('Do you want to save changes?\n\t\tNO - disagree\n\t\tWhatever else - agree\n')
        if res != 'NO':
            PhoneBook.writeToFile()
            exit()
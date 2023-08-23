class Contact:
    def __init__(self):
        """constructor of Contact class"""
        self.__attr: dict = {
            "first_name": None,
            "last_name": None,
            "middle_name": None,
            "organization_name": None,
            "work_phone": None,
            "personal_phone": None
        }

    @staticmethod
    def getReadyString(dst: str) -> str:
        """Makes a string easy to put in a table for readability
        
        Arguments:
            dst: str - full string
        Returned value:
            str - string with len() = 10;

        If dst is None -> return "   None   "
        If len() == 10 -> return same string as getted as argument
        If len() > 10 -> cut string to 9 chars, than add one dot to show that string longer than we see
        If len() < 10 -> add spaces in  the end of string until len() != 10

        """
        res: str = ""
        
        if dst is None:
            return "   None   "
        if len(dst) > 10:
            res = dst[:9]
            res += '.'
        else:
            res = dst

        while len(res) < 10:
            res += ' '
        return res


    def printContact(self):
        """Print contact in short form as a part of the table"""
        toPrint: str = "|"
        for at in self.__attr:
            toPrint += self.getReadyString(self.getAttr(at)) + "|"
        print(toPrint)

    def inspectContact(self):
        """Print full info of contact"""
        for at in self.__attr:
            print(at + ':', self.__attr.get(at))

    def setAttr(self, which: str, value: str):
        """Set attribute of contact
        
        Arguments:
            which: str -> which attribute want to set
            value: str -> which value want to set
        No returned value

        If value is empty string -> set None as attribute

        """
        if value is not None and len(value) == 0:
            value = None
        self.__attr[which] = value

    #getters
    def getAttr(self, which: str):
        """Return 'which' attribute """
        return self.__attr.get(which)

    def getAttrs(self):
        """return all attributes"""
        return self.__attr
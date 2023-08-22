class Contact:
    def __init__(self):
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
        toPrint: str = "|"
        for at in self.__attr:
            toPrint += self.getReadyString(self.getAttr(at)) + "|"
        print(toPrint)

    def inspectContact(self):
        for at in self.__attr:
            print(at + ':', self.__attr.get(at))

    def fillFields(self, attr: list):
        self.setFirstName(attr[0])

    def setAttr(self, which: str, value: str):
        if value is not None and len(value) == 0:
            value = None
        self.__attr[which] = value

    #getters
    def getAttr(self, which: str):
        return self.__attr.get(which)

    def getAttrs(self):
        return self.__attr
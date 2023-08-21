class Contact:
    def __init__(self):
        self.__firstName: str = None
        # lastName = None
        # middleName = None
        # organizationName = None
        # workPhone = None
        # personalPhone = None

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
        toPrint = "|"
        toPrint += self.getReadyString(self.__firstName) + "|"
        print(toPrint)

    def inspectContact(self):
        print(f'First name: {self.__firstName}')

    def fillFields(self, attr: list):
        self.setFirstName(attr[0])

    # setters
    def setFirstName(self, firstName):
        self.__firstName = firstName

    # def setLastName(self, lastName):
    #     self.lastName = lastName

    # def setMiddleName(self, middle):
    #     self.middle = middle

    # def setOrgName(self, organizationName):
    #     self.organizationName = organizationName

    # def setWorkPhone(self, workPhone):
    #     self.workPhone = workPhone

    # def setPersonalPhone(self, personalPhone):
    #     self.personalPhone = personalPhone

    #getters
    def getFirstName(self) -> str:
        return self.__firstName

    # def getLastName(self, lastName) -> str:
    #     self.lastName = lastName

    # def getMiddleName(self, middle) -> str:
    #     self.middle = middle

    # def getOrgName(self, organizationName) -> str:
    #     self.organizationName = organizationName

    # def getWorkPhone(self, workPhone) -> str:
    #     self.workPhone = workPhone

    # def getPersonalPhone(self, personalPhone) -> str:
    #     self.personalPhone = personalPhone
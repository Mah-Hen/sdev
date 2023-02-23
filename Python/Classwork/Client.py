from Person import Person

class Client(Person):
    __contract = None

    def __init__(self, name, address, birthday, contract):
        super().__init__(name, address, birthday)
        self.__contract = contract

    def __str__(self):
        return super().__str__() + "\n\t{}".format(self.__contract)
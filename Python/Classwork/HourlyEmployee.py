# Child class
from Employee import Employee

class HourlyEmployee(Employee):
    __hourlywage = None

    def __init__(self, name, id, title, wage):
        super().__init__(name, id, title)
        self.__hourlywage = wage

    def setWage(self, wage):
        self.__hourlywage = wage

    def getWage(self):
        return self.__hourlywage

    def __eq__(self, e2):
        return super().__eq__(e2) and self.__hourlywage == e2.__hourlywage

    def __str__(self):
        Parentstr = super().__str__()
        return Parentstr + "\nWage: {}".format(self.__hourlywage)
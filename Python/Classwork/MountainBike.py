# Child class

from Bicycle import Bicycle

class MountainBike(Bicycle): #Dont use extend like java, but instead place the parent class in parentheses.
    __seatHeight = None


    def __init__(self, gear, speed, seatHeight) -> None:
        super().__init__(gear, speed)
        self.__seatHeight = seatHeight


    def setHeight(self, seatHeight):
        self.__seatHeight = seatHeight

    def getHeight(self):
        return self.__seatHeight

    def __str__(self):
        return super().__str__() + "\nseat height is "\
            + str(self.__seatHeight)

    def __eq__(self, bk2):
        return super().__eq__(bk2) and self.__seatHeight == bk2.__seatHeight
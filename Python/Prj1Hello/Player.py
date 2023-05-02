class Player:
    __name = None
    __health = 0
    __inventory = []

    def __init__(self, name):
        self.__name = name
        self.__health = 4
        self.__inventory = []

    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setHealth(self, health):
        self.__health = health

    def getHealth(self):
        return self.__health
    
    def decHealth(self, damage):
        self.__health -= damage

    def incHealth(self, up):
        self.__health += up

    def addInventory(self, item):
        self.__inventory.append(item)

    def removeInventory(self, item):
        self.__inventory.remove(item)

    def displayInventory(self):
        print("INVENTORY:")
        for item in self.__inventory:
            print(item, "\t")

    
    def __str__(self):
        return "{}\nHealth:{}".format(self.__name, self.__health)
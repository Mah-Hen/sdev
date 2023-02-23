#Parent Class
class Employee:

    __name = None
    __id = None
    __title = None

    def __init__(self, name, id, title):
        self.__name = name
        self.__id = id
        self.__title = title

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setID(self, id):
        self.__id = id

    def getID(self):
        return self.__id
    
    def setTitle(self, title):
        self.__title = title
    
    def getTitle(self):
        return self.__title

    def __eq__(self, e2):
        return self.__name == e2.__name and self.__id == e2.__id and self.__title == e2.__title
    
    def __str__(self):
        return "Name: {}\nID #: {}\nTitle: {}".format(self.__name, self.__id, self.__title)
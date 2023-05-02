class Alert:
    __level = ""
    __message = ""

    def __init__(self, level, message):
        self.__level = level
        self.__message = message


    def getLevel(self):
        return self.__level

    def setLevel(self, lvl):
        self.__level = lvl

    def getMessage(self):
        return self.__message

    def setMessage(self, msg):
        self.__message = msg


    def increaseLevel(self):
        if self.__level == "Yellow":
            self.__level = "Orange"
        elif self.__level == "Orange":
            self.__level = "Red"
        else:
            self.__level = "Red"


    def decreaseLevel(self):
        if self.__level == "Red":
            self.__level = "Orange"
        elif self.__level == "Orange":
            self.__level = "Yellow"
        else:
            self.__level = "Yellow"


    def __eq__(self, obj):
        return self.__message == obj.__message

    def toString(self):
        return "*****{:s} alert*****\n{:s}\n*******************".format(self.__level, self.__message)




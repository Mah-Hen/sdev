class Box:  #From box import box is obtaining the Box file and importing the box class
    __size = None    # underscore underscore makes it private. Just like private variable in Java
    __contents = None
    __sym = "*"

    def _init_(self, args):
        if len(args) == 0:
            self.__size = 4
            self.__contents = ""
        elif len(args) == 2:
            self.__size = args[0]
            self.__contents = args[1]
            self.fixSize()
        else:
            raise Exception("Invalid Constructor")

    
    def getSize(self):
        return self.__size

    
    def getContents(self):
        return self.__contents


    def setSize(self, size):
        self.__size = size
        self.__fixSize()
    

    def setContents(self, contents):
        self.__contents = contents
        self.__fixSize()

    def __fixSixe(self):
        actual = len(self.__contents) + 4
        self.__size = max(actual, self.__size)

    def __str__(self) -> str:
        theSym = Box.__sym
        out = ""
        for i in range(self.__size):
            out += theSym
        out += "\n"
        out += theSym + " " + self.__contents + " "
        spaces = self.__size - len(self.__contents) - 4
        for i in range(spaces):
            out += " "
        out += theSym + "\n"
        for i in range(self.__size):
            out += theSym
        
        return out

    def equals(self,b2):
        if self.__contents == b2.__contents:
            return True
        else:
            return False
    
    def setSymbol(s):   #Methods like these don't use self because they're not modifying anything
        Box.__sym = s   #Self is going to be used in methods that are being used or instances.

class Table:
    __tab = None
   

    def __init__(self, rows, cols):
        self.__cols = cols
        self.__rows = rows
        self.__tab = [[' ' for j in range(cols)] for i in range(rows)]

    def setChar(self, row, col, char):
        self.__tab[row][col] = char

    def getChar(self, row, col):
        return self.__tab[row][col]

    def __eq__(self, t1):
        return self.__rows == t1.__rows and self.__cols == t1.__cols

    def __str__(self):
        return "\n".join(["".join([str(cell) for cell in row]) for row in self.__tab]) #This will create a list of strings, where each string is a row in the table separated by tabs, and then join the strings with newline characters to create the final output string.

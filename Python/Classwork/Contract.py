class Contract():
    __Cnumber = None
    __Cdetails = None 


    def __init__(self, number, details):
        self.__Cnumber = number
        self.__Cdetails = details 

    def __str__(self):
        return "CONTRACT FOR LEGAL SERVICES\n\t\t{}\n{}".format(self.__Cnumber, self.__Cdetails)   
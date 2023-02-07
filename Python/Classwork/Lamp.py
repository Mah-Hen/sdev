'''
Mahlaki Henry
2/6/2023
This is my original work
'''
class Lamp:
    __isOn = None

    def __init__(self, *args):
        if len(args) == 1:
            self.__isOn = args[0]
        elif len(args)==0:
            self.__isOn = False
        else:
            raise Exception ("Invalid Constructor")


    def turnOn(self):
        self.__isOn = True


    def turnOff(self):
        self.__isOn = False


    def flip(self):
        self.__isOn = not self.__isOn


    def isOn(self):
        return self.__isOn


    def setLamp(self, isOn):
        self.__isOn = isOn


    def __eq__(self, other: object):
        return self.__isOn == other.__isOn


    def __str__(self) -> str:
        
        out = None
        if self.__isOn:
            out = "On"
        else:
            out = "Off"
        out = "{0:3s} ".format(out)
        
        return out

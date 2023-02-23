# Parent Class

class Bicycle:  
    __gear = None
    __speed = None


    def __init__(self, gear, speed):
        self.__gear = gear
        self.__speed = speed


    def applyBrake(self, decrement):
        self.__speed -= decrement

    def speedUp(self, increment):
        self.__speed += increment

    def __str__(self):
        newstr = "No of gears are " + str(self.__gear) + "\n" + \
            "speed of bike is " + str(self.__speed)
        return newstr
    
    def __eq__(self,b2):
        return self.__gear ==  b2.__gear and self.__speed == b2.__speed
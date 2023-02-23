class Counter:
    __count = 0
    __step = 0
    __origCounter = 0
    __origStep = 0

    def __init__(self, origCount, origStep, count, step):
        self.__count = count
        self.__step = step
        self.__origCounter = origCount
        self.__origStep = origStep

    def getCount(self):
        return self.__count

    def setCount(self, count):
        self.__count = count

    def getStep(self):
        return self.__step

    def setStep(self, step):
        self.__step = step

    def inc(self):
        self.__count += self.__step
    
    def dec(self):
        self.__count -= self.__step

    def reset(self):
        self.__count = self.__origCounter
        self.__step = self.__origStep

    def __str__(self):
        return "Counter ({}, {})".format(self.__count, self.__step)

    def __eq__(self, c2):
        return self.__count == c2.__count and self.__step == c2.__step
class Story():
    __choice = None
    __name = None

    def __init__(self, choice, name):
        self.__choice = choice
        self.__name = name

    
    def Prompt1(self):
        return f"\t*PLOP*\n{self.__name} finds themself wandering in a dense forest, unsure of how they got here.\nWandering around for serveral minutes, {self.__name} finally comes across a fork in the path.\nTo {self.__name}'s left (1), a path that lead to a dark, ominous cave.\nTo {self.__name}'s right (2), the path leads to a beautiful, serene lake."
    
    def Choice1(self):
        if self.__choice == 1:
            return f"As{self.__name} enters the cave, it's barely lit, with a distant ember in the background.\n*SWOOOSSH*, a chilling wind follows behind as {self.__name} creeps closer inside the barely lit cave.\nGuided by a shiny image {self.__name} encounters a horde of goblins ready to attack.\n{self.__name} can either fight them off (1) or run away (2)."
        else:
            return f"{self.__name} encounters a beautiful sight of sirens swimming in the lake.\nAs you approah, you notice a magical fairy sitting on a nearby rock.\nThe magical fairy clamors out, \"*hehe* I can grant you one wish, BUUUT the wish is a wish of MY choosing.\n\"Don't worry *hehe*\", she says, \"it will be beneficial for your journey!\"\nSelect from one of five wishes (1-5)"
    
    def Prompt2(self):
        return f"{self.__name} continues to wander through the forest. As the sun starts to set, {self.__name} comes across a small cottage.\
            \nAs {self.__name} knocks on the door, a dusty old woman opens it and invites them inside.\nShe offers {self.__name} a warm meal and a bed to sleep in for the night.\
            \nHowever, as {self.__name} eats their meal, their eyelids starts to bend to gravity and {self.__name} beings to feel drowsy.\nPast the brink of no return {self.__name} finally realizes too late that the dust old woman has poisoned them.\
            \nPassed out on a refrigerator cold concrete slab, undreaded weariness fell upon the mind of the young {self.__name}.\
            \n{self.__name} awakes and finds themself locked in a small room.\
            \n{self.__name} stands up but almost topples over, not yet recovered from the unindentified poison. {self.__name} scans the room to look for a way out and there they spot it. A keypad on door that leads to some unknown area.\
            \n{self.__name} walks up to the keypad and sees that it has a 4 digit code to it, aswell as a hint to guessing the code.\
            \n{self.__name} can either (1) try to escape or (2) try the odds with the old woman"
    
    def Choice2(self):
        if self.__choice == 1:
            print(f"{self.__name} decides to take a crack at the keypad. Reading the hint on the pad,\n\"Can you find the four digit number in which the first digit is one fourth of the last digit, the second digit is 6 times the first digit, and the third digit is the second digit plus 3?\"")
            

        
        else:
            print(f"{self.__name} decides to take his chances in the prison. Over the course of an inconceivable amount of time, the old woman, whom {self.__name} refers to as the old crow, has been plumping {self.__name} up. Feeding them a whopping 5 meals a day.\n\
            The meals consisting of porride, bread, and some mystery meat. Unappetizing the meal is, they just can't seem to stop eating it.\nOnce {self.__name}'s shirt got passed the bell button the stomach, the old woman knew it was time.\n\
            Up and early the old woman got them, didn't even allow for an execution date, just did it the next morning.")
        
    
    def Prompt2_5(self):
        print(f"The old woman comes into the cellar and grabs {self.__name} by the hair. Locking a clump of it around her fingers. Dragging ")
        
        pass


    def Prompt3(self):
        return f""
    
    def Choice3(self):
        return f""


    def setChoice(self, choice):
        self.__choice = choice

    def getChoice(self):
        return self.__choice
    
    def getKeypadEntry(self):
        limit = 3
        limitCounter = 0
        cEntry = 1694
        chances = limit-limitCounter

        print(f"You got {chances} chances")
        while limitCounter < limit: 
            entry = input(" ").strip()
            if entry.isnumeric():
                entry = int(entry)
                if entry == cEntry:
                    limitCounter = 3
                    return 0
                else:
                    print("*ERR*")
                    limitCounter += 1
                    chances = limit-limitCounter
                    print(f"You got {chances} chances left.")
            else:
                print("*ERR*")
                limitCounter += 1
                chances = limit-limitCounter
                print(f"You got {chances} chances left.")
                
        
        return -1

    
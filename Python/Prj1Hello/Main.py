from Table import Table
from Player import Player
from Story import Story
import os
import time
import random

table  = Table(3,3)
name = "Y"
P1 = Player(name)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def disclaimer():
    print("Welcome To A Basic Text Adventure Game!\nHere you will go through a story that will set the mood and feelings of a real game! Hopefully.\nThis is a linear game so far. The introduction is controlled by numbers and as you progress, you'll face puzzles against the NPCs!\nOverall this a feedback game, so please give me feedback.\n\tENJOY! ")

def decide():
    print()
    while True:
        choice = input("Decide: ")
        if choice.isnumeric():
            choice = int(choice)
            if choice < 10 and choice > 0:
                return choice
            else:
                print("Not Valid!")
        else: 
            print("Not Valid")

def roll():
    return random.randint(1,3)

def getStory():
    story = Story(0,name)
    print(story.Prompt1())
    choice = decide()
    if choice == 1:
        story.setChoice(choice)
        time.sleep(1)
        clearScreen()
        print(story.Choice1())
        choice = decide()
        if choice == 1:
            print(f"{name} decides to attack the horde of goblins.")
            if roll() == 1:
                P1.decHealth(roll())
                print(f"{name} beaten the goblins off with his barehands. Suffering {P1.getHealth()} damage to they're health. Goblins are very territorial, yet there shouldn't be this many goblins guarding something unless it is very lucrative...\nALOR! A Treasure Chest!")
            elif roll() == 2:
                P1.decHealth(roll())
                print(f"{name} has suffered {P1.getHealth()} damage to they're health. Causing a retreat.")

            else:
                print(f"{name} suffered immense injuries as a result of being surronded by the horde.\nThis is a 1 out of every 3 chance of goblins being this smart enough. As result, all of {name}'s health depleted.")
                time.sleep(2)
                clearScreen()
                # More
        else:
            print(f"{name} decided that goblins are not a force to be reckon with just barehands. As a result {name} ran away from the horde, out of the cave and ventured on down the forest.")
            time.sleep(1.5)
            clearScreen()
            print(story.Prompt2())
            choice = decide()
            time.sleep(1)
            clearScreen()
            story.setChoice(choice)
            entry = story.Choice2()
            if entry == 0:
                print(f"*click*")
                story.Prompt3()
            else:
                print(f"*BEEP*\t*BEEP*\n\"Locked out.\" The hint changed to.")





    elif choice == 2:
        story.setChoice(choice)
        time.sleep(1)
        clearScreen()
        print(story.Choice1())
        choice = decide()
        if choice == 1:
            P1.incHealth(roll())
            print(f"\"Ah, you chose wish number 1. *teehee*\nAlrighty then here you go, Enjoy!\" the Fairy said.\n \"You got some more health\"\nHealth: {P1.getHealth()}")
        elif choice == 2:
            P1.addInventory("Sandwich")
            print(f"*Hehe* \"Number 2... interesting choice\nNot really, you get a... sandwich, Enjoy!\" The fairy giggled\n")
            P1.displayInventory()
        elif choice == 3:
            P1.addInventory("HINT")
            print(f"\"ooooooh, what a lucky soul you are, you get some help later on, Enjoy!\" the fairy sounding slightly brittle\n")
            P1.displayInventory()
        elif choice == 4:
            print(f"Health: {P1.getHealth()}")
            P1.decHealth(roll())
            print(f"Oops! Wrong choice! *hehe* your health decreases by {roll()} but that's okay because...,\" fairy said provocatively, \"You're still alive!\"\nHealth: {P1.getHealth()}")
        else:
            print("\"Wish number 5 is a teleportation wish. I am going to send you to some place anywhere in a 10 mile radius. Enjoy!\" the fairy said with a michevous grin.")
            # dealbreaker, shorty story or long story depending on where you got teleported.
            time.sleep(4)
            clearScreen()
            print(f"*PLOP*\n\"Teleported to who knows where! There's trees for miles and miles!\" {name} growled.\nAnd so {name} continues on this prison in Wonderland")
            time.sleep(5)
            clearScreen()
            print(story.Prompt2())
            choice = decide()
            clearScreen()
            story.setChoice(choice)
            story.Choice2()
            Entry = story.getKeypadEntry()
            if Entry == 0:
                print(f"*click*\n")
                story.Prompt3()
            else:
                print(f"*BEEP*\t*BEEP*\n\"Locked out.\" The hint changed to.")
                story.setChoice(choice=2)
                story.Choice2()


            

    else:
        print()
        getStory()
    



'''
def setTable():
    table.setChar(0,0,'|')
    table.setChar(0,1,'')
    table.setChar(0,2,'|')
    table.setChar(1,0,'|')
    table.setChar(1,1,'')
    table.setChar(1,2,'|')
    table.setChar(2,0,'|')
    table.setChar(2,1,'')
    table.setChar(2,2,'|')
'''

def getPlayer():
    name = str(input("First what would you like to be called? ")) 
    print("Congrats, {}! This is what you'll be referred to from this point on.".format(name))

    P1 = Player(name)
    return P1

def main():
    #disclaimer()
    #time.sleep(15)
    #clearScreen()
    getStory()
    '''
    setTable()
    player = getPlayer()
    time.sleep(10)
    clearScreen()
    '''
    


main()
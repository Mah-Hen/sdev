'''
Mahlaki Henry
2/6/2023
This is my original work
'''
from Lamp import Lamp
import random


def display(lamps):
    count = 1
    for i in range(30):
        print(lamps[i], end="\t")
        if count%5==0:
         print()
        count+=1

def main():
    lamp1 = Lamp()

    lamps = [Lamp() for i in range(30)]
    
    for lamp in lamps:
        rand = random.randint(0,1)
        lamp.setLamp(rand)
    
    display(lamps)
    print("---------")
    print("---------")
    
    for j in range(len(lamps)):
        if(j<=9):
            lamps[j].flip()  
        elif(j<20 and j>=10): 
            lamps[j].turnOff()
        else:
            lamps[j].turnOn(); 
        
    display(lamps)



main()
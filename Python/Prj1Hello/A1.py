'''
Mahlaki Henry
1/18/2022
Homework 1
This is my own original work
'''
import math




def computeVals(listX):
    newList = []
    for i in range (len(listX)):
        sqr = listX[i]**2
        y = math.sin(listX[i]) + math.sin(sqr)
        formatY = "{:.2f}".format(y)   # move format into display() function
        newList.append(formatY)
        
    return newList

def display(listY):
    cols = 7
    length = len(listY)
    rows = int(length/cols)

    for i in range(rows):
        table = listY[i*cols : i*cols + cols]
        print(*table)    
        
def main():
    listX = [.5*x for x in range (0, 21)]
    listY = computeVals(listX)
    display(listY)
    

main()
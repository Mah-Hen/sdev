from stack import stack

Stack = stack()


    

    
def isBalanced(expression):
    opening_types = set(['(', '[', '{', '<'])
    closing_types = set([')', ']', '}', '>'])
    matching_pairs = set([('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')])


    for char in expression:
        if char in opening_types:
            Stack.push(char)
        elif char in closing_types:
            if len(Stack) == 0:
                return False
            opening = Stack.pop()
            pair = (opening, char)
            if pair not in matching_pairs:
                return False

    return len(Stack) == 0

        
        #for i in range(len(Stack)):
        #    if Stack.peek() == 
        #    match = re.search()

def getInput():
    xprsn = input("Please enter an expression: ").strip()


    return xprsn

def main():
    expression = getInput() # (a+b)*((c+d)*14)
    print("Entry:", expression)
    if(isBalanced(expression)):
        print("Balanced")
    else:
        print("Not balanced")
    
   
    


main()
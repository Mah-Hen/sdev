from Counter import Counter

def main():
    
    count = Counter(1, 1, 1, 4)
    print(count.getStep())
    print(count.getCount())
    count.setCount(0)
    count.inc()
    print(count) #no need to call the string method bc ______
    c2 = Counter(1, 1, 3,10)

    if(count.__eq__(c2)):
        print("Equal")
    else:
        print("Not Equal")

    count.reset()
    c2.reset()

    if(count.__eq__(c2)):
        print("Equal")
    else:
        print("Not Equal")
    


main()
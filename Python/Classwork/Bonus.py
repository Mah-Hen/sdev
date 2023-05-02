from Alert import Alert
def main():
    a = Alert("Red", "A tornado")
    print(a.toString())

    print()

    level = a.getLevel()
    print("Level: ", level)
    message = a.getMessage()
    print("Message: ", message)

    print()

    a.setLevel("Yellow")
    a.setMessage("A Tropical Storm")
    print(a.toString(), "\n" )
    a.increaseLevel()
    print("Increase:\n", a.toString())
    a.decreaseLevel()
    print("Decrease:\n", a.toString())


    b = Alert("Orange", "An Earthquake")
    print(a.__eq__(b))
    a.increaseLevel()
    a.setMessage("An Earthquake")
    print(a.__eq__(b))




main()


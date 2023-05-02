from Card import Card
from Deck import Deck

'''
Mahlaki Henry
2/6/2023
This is my original work
'''

count1 = []
count2 = []
count0 = []



def createDeck():
    cards = [Card(v, s) for v in range(1, 14)
             for s in "HCDS"]  # Hearts, Cloves, Diamonds, Spades
    deck = Deck("Deck", cards)
    deck.setCols(4)
    deck.shuffle()
    return deck, len(cards)


def compareCards(c1, c2, deck):
    if c1 is None or c2 is None:
        return -1
    else:
        if c1.getSuit() == 'S' and c2.getSuit() != 'S':
            return 1
        elif c1.getSuit() != 'S' and c2.getSuit() == 'S':
            return 2
        elif c1.getSuit() == 'S' and c2.getSuit() == 'S':
            if c1.getValue() > c2.getValue():
                return 1
            elif c1.getValue() < c2.getValue():
                return 2
            else:
                return 0
        elif c1.getSuit() != 'S' and c2.getSuit() == 'S':
            return 2
        else:
            if c1.getValue() > c2.getValue():
                return 1
            elif c1.getValue() < c2.getValue():
                return 2
            else:
                return 0


def playGame(hand1, hand2, nplay, deck):
    rCount = 0
    numCardsPlayed = 0

    while not hand1.isEmpty() and not hand2.isEmpty():
    #for i in range(nplay):
        c1 = hand1.getFirst()
        c2 = hand2.getFirst()

        print("Cards Played:", c1, c2)
        result = compareCards(c1, c2, deck)
        numCardsPlayed += nplay
        if result != -1:
            results(result)
        #hand1.getFirst()
        #hand2.getFirst()
        '''
    if hand1.isEmpty():
        return 2
    elif hand2.isEmpty():
        return 1
    else:
        return 0
        '''


def results(result):
    global count1, count2, count0

    if result == 1:
        print("P1")
        count1.append(result)
    elif result == 2:
        print("P2")
        count2.append(result)
    else:
        print("=")
        count1.append(result)
        count2.append(result)
        count0.append(result)

def congrats():
    if len(count1) != len(count2):
        if len(count1) > len(count2):
            print(count1, count2)
            return "\nPlayer 1 wins the Game!"
        elif len(count2) > len(count1):
            print(count1, count2)
            return "\nPlayer 2 wins the Game!"
        else:
            print(count1, count2)
            print(len(count1), len(count2))
            return "\nTie Game!"
    
    else:
        print(count1, count2)
        print(len(count1), len(count2))
        return "\nTie Game!"
    


def main():
    numCardPlay = 1
    deck, length = createDeck()
    print(deck, "\n", length)
    num = 0

    while num < length:
        hand1, hand2 = deck.deal(numCardPlay, 2)
        print(hand1)
        print(hand2)

        playGame(hand1, hand2, numCardPlay, deck)
        print(len(count1), len(count2), "\n")
        num += numCardPlay * 2
    #print(indicator)
    '''
    if indicator == 0:
        print("Tie game with",len(count0))
    if indicator == 1:
            print("P1 game with",len(count1))
    if indicator == 2:
            print("P2 game with",len(count2))
    '''
    lSum = len(count1) + len(count2) - len(count0)
    print(congrats())
    print(lSum, "Rounds played")
    '''
    if len(count1) != len(count2) or len(count1) != len(count0) or len(count2) != len(count0):
        if len(count1) > len(count2) and len(count1) > len(count0):
            print(count1, count2, count0)
            return "\nPlayer 1 wins the Game!"
        elif len(count2) > len(count1) and len(count2) > len(count0):
            print(count1, count2, count0)
            "\nPlayer 2 wins the Game!"
        else:
            print(count1, count2, count0)
            print(len(count1), len(count2), len(count0))
            return "\nTie Game!"
    
    else:
        print(count1, count2, count0)
        print(len(count1), len(count2), len(count3))
        return "\nTie Game!"
    '''


main()

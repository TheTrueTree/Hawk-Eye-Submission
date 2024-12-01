from enum import IntEnum, Enum
import random

class suits(Enum):
    S = 'Spades'
    C = 'Clubs'
    H = 'Hearts'
    D = 'Diamonds'
    J = 'Jokers'

class cardValues(IntEnum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Joker = 14

    def __eq__(self, other):
        return self.value == other.value

class card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __eq__(self, other):
        return (self.number == other.number) and (self.suit == other.suit)

    def __lt__(self, other):
        if(self.number.value < other.number.value):
            return True
        elif (self.number.value > other.number.value):
            return False
        else:
            if(self.suit.value == 'Spades'):
                return True

            elif(self.suit.value == 'Clubs'):
                if(other.suit.value in ('Hearts', 'Diamonds', 'Jokers')):
                    return True
                else: return False

            elif(self.suit.value == 'Hearts'):
                if(other.suit.value in ('Diamonds', 'Jokers')):
                    return True
                else: return False
            elif(self.suit.value == 'Diamonds'):
                if(other.suit.value in ('Jokers')):
                    return True
                else: return False
            else:
                return False

class deck:
    cards = []
    decksize = 52
    cardOrder = []

    def __init__(self, joker):

        if(joker == 1):
            self.decksize = 54
        
        self.cardOrder = [x for x in range(self.decksize)]

        for number in cardValues:
            if(number.value == 14 and joker == 0):
                continue
            for suit in suits:
                if((number.value != 14 and suit.value != 'Jokers') or (number.value == 14 and suit.value == 'Jokers')):
                    self.cards.append(card(number, suit))
                    if(number.value == 14):
                        self.cards.append(card(number, suit))

    def printDeck(self):
        for x in range(0, len(self.cards)):
            print(self.cards[x].number.name, 'of', self.cards[x].suit.value)
    
    def printCard(self, position):
        print(self.cards[position].number.name, 'of', self.cards[position].suit.value)

    def shuffle(self):
        self.cardOrder = [x for x in range(self.decksize)]
        random.shuffle(self.cardOrder)

    def drawCard(self):
        cardDrawn = self.cards[self.cardOrder[0]]
        del self.cardOrder[0]
        return cardDrawn

    def addCard(self, newCard):
        self.decksize = self.decksize + 1
        self.shuffle()

        for x in range(0, self.decksize):
            if not(self.cards[x] < newCard):
                self.cards.insert(x, newCard)
                break
    
    def removeCard(self, newCard):
        self.decksize = self.decksize - 1
        self.shuffle()
        
        for x in range(0, self.decksize):
            if (self.cards[x] == newCard):
                self.cards.pop(x)
                break

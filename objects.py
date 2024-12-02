from enum import IntEnum, Enum
import random

class suits(Enum):
    S = 'Spades'
    C = 'Clubs'
    H = 'Hearts'
    D = 'Diamonds'
    J = 'Jokers'

class cardValues(IntEnum):
    Null = 0
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

class card:
    def __init__(self, number, suit, pos):
        self.number = number
        self.suit = suit
        self.position = pos

    def __eq__(self, other):
        return (self.number == other.number) and (self.suit == other.suit)

    def __lt__(self, other):
        if(self.number < other.number):
            return True
        elif (self.number > other.number):
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
    
    def simplify(self, card):
        if(card < 11 and card > 1):
            return card
        elif(card == 1):
            return 'A'
        elif(card == 11):
            return 'J'
        elif(card == 12):
            return 'Q'
        elif(card == 13):
            return 'K'
        elif(card == 14):
            return 'X'
        
    def getGameCard(self):
        return '[' + str(self.simplify(self.number.value)) + self.suit.name + ']'
    
    def updatePosition(self, newPos):
        self.position = newPos

class deck:
    cards = []
    decksize = 52
    cardOrder = []

    def __init__(self, joker):
        if(joker == 1):
            self.decksize = 54
        
        self.cardOrder = [x for x in range(self.decksize)]

        y = 0
        for number in cardValues:
            if((number.value == 14 and joker == 0) or number.value == 0):
                continue
            for suit in suits:
                if((number.value != 14 and suit.value != 'Jokers') or (number.value == 14 and suit.value == 'Jokers')):
                    self.cards.append(card(number, suit, y))
                    y = y + 1
                    if(number.value == 14):
                        self.cards.append(card(number, suit))
                        y = y + 1
        
        self.shuffle()

    def printDeck(self):
        for x in range(0, self.decksize):
            print(self.cards[x].getGameCard(), end=' ')
    
    def printCard(self, position):
        print(self.cards[position].number, 'of', self.cards[position].suit.value)

    def shuffle(self):
        self.cardOrder = [x for x in range(self.decksize)]
        random.shuffle(self.cardOrder)

    def drawCard(self):
        if(len(self.cardOrder) < 1):
            self.shuffle()
        cardDrawn = self.cards[self.cardOrder[0]]
        del self.cardOrder[0]
        return cardDrawn

    def addCard(self, newCard):
        added = False
        self.decksize = self.decksize + 1
        self.shuffle()
        newDeck = []

        for x in range(0, self.decksize - 1):
            if not(self.cards[x] < newCard):
                if not(added):
                    newDeck.append(card(newCard.number, newCard.suit, x))
                    added = True
                if(x <= self.decksize - 1):
                    newDeck.append(card(self.cards[x].number, self.cards[x].suit, x+1))
            else:
                newDeck.append(card(self.cards[x].number, self.cards[x].suit, x))

        self.cards = newDeck
                
    def removeCard(self, newCard):
        self.decksize = self.decksize - 1
        self.shuffle()
        
        for x in range(0, self.decksize):
            if (self.cards[x] == newCard):
                self.cards.pop(x)
                break

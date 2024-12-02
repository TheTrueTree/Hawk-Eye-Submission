import time
from objects import *

class Game:
    # Initiaising the Game
    def __init__(self, Jokers):
        self.playerDeck = deck(Jokers)
        self.Jokers = Jokers
        self.experience = 0
        self.health = 20
        self.healthMax = 20
    
    #Basic logic for opponent to pick highest card in their hand
    def pickCard(self, cards):
        max = 0
        ind = 0
        for x in range(0, len(cards)):
            if(cards[x].position > max):
                max = cards[x].position
                ind = x

        return cards[ind], ind
    
     #Code for player to shuffle and discard hand
    def newHand(self):
        newHand = []
        self.playerDeck.shuffle()

        for x in range(0, 4):
            newHand.append(self.playerDeck.drawCard())

        print('Your new Hand:')
        for x in range(0, len(newHand)):
            print(newHand[x].getGameCard(), end=' ')
        
        newHand.append(card(0, suits.S, 0))
        return newHand
    
    def generateOptions(self):
        choices = random.choices([1, 2, 3], [0.35, 0.4, 0.25])[0]
        realOptions = []

        for x in range(choices):
            y = random.choices(['X', 'F'], [0.8, 0.2])[0]
            realOptions.append(y)
        
        return realOptions
    
    #Text heavy introduction
    def tutorial(self):
        print("This game is pretty simple! You draw 5 cards and take turns playing a card.")
        time.sleep(1)
        print("Your opponent plays a card as well. Whoever played the higher card deals the")
        time.sleep(1)
        print("difference in score to their opponent as damage.")
        time.sleep(1)
        print("")
        print("You have been given a standard deck of", self.playerDeck.decksize, "cards, but win enough and you can")
        time.sleep(1)
        print("potentially earn some more! If you understand, enter [1] to try out a game!")
        time.sleep(1)
        print("If you need more time, select [2] and we can run through it again.")
        
        self.tutorialDirectory(input(''))

    #Restart tutorial logic
    def tutorialDirectory(self, option):
        if(str(option) == '1'):
            self.tutorialGame()
        elif(str(option) == '2'):
            self.tutorial()
        else:
            print("Please try that again.")
            self.tutorialDirectory(input(''))

    #Setup for tutorial Game
    def tutorialGame(self):
        
        opponentDeck = deck(self.Jokers)
        playerHand = []
        opponentHand = []

        for x in range(0, 5):
            playerHand.append(self.playerDeck.drawCard())
            opponentHand.append(opponentDeck.drawCard())
        
        
        self.mainTutorial(playerHand, opponentHand, opponentDeck)

    def mainTutorial(self, pHand, oHand, oDeck):
        oppHealth = 10
        

        time.sleep(1)
        print("The turn will begin with your health shown, and your hand being drawn, like below:")
        print("Health: ", self.health, '/', self.healthMax, sep='')

        for x in range(0, len(pHand)):
            print(pHand[x].getGameCard(), end=' ')

        print("")
        

        time.sleep(1)
        
        print("Now you just need to select your card! Simply put down a number from 1 to 5. If you don't like any card simply type 'S' to shuffle and redraw 4 cards. Bewarned that this gives your opponent a free shot.")
        print("Note: We are playing with Ace as low.")
        
        while True:
            decision = input('')
            if(decision != 'S'):
                try:
                    print('You selected:', pHand[int(decision)-1].getGameCard())
                    uChoice = pHand[int(decision)-1]
                    break
                except (ValueError, IndexError):
                    print("Try that again!")
            else:
                print('You shuffled!')
                self.newHand()
                uChoice = card(1, suits.S, 0)
            
        print("Now, your opponent will also pick a card!")

        time.sleep(1)
        

        opChoice, indic = self.pickCard(oHand)
        print('They selected:', opChoice.getGameCard())

        print('So in this scenario, the difference would be found, and damage dealt to the loser.')
        if(uChoice> opChoice):
            diff = uChoice.number - opChoice.number
            print("You Won! So ", diff, " damage would be done to them, taking them to ", oppHealth - diff, ' health out of ', oppHealth, sep='')
        elif(uChoice== opChoice):
            print("It seems you drew! Nothing happens and you get your next turn.")
        else:
            diff = opChoice.number - uChoice.number
            print("You lost! So ", diff, " damage would be done to you, taking you to ", self.health - diff, ' health', sep='')
        
        print("That ends the tutorial, there may be more features to discover, but if you'd like to replay this, enter 1. If not 2 will let you start the game!")
        a = input("")
        

        if(str(a)== "1"):
            self.tutorialGame()
        else:
            self.mainGameStart()

    def fire(self):
        playerHand = []
        gained = 0

        print("You have drawn three cards! Which one would you like to burn in the fire raging in front of you?")
        
        for x in range(0, 3):
            playerHand.append(self.playerDeck.drawCard())
            print(playerHand[x].getGameCard(), end=' ')
        
        print("")
        while True:
            y = input("Select the card to burn! ")
            try:
                self.playerDeck.removeCard(playerHand[int(y)-1])
                break
            except (ValueError, IndexError):
                print("Please try again")

        print("What a pretty fire, the heat slowly brings feeling back to your cold face.")
        self.health = self.health + playerHand[int(y)-1].number
        if(self.health > self.healthMax):
            gained = playerHand[int(y)-1].number - (self.health - self.healthMax)
            self.health = self.healthMax
        else:
            gained = playerHand[int(y)-1].number
        print("You gained ", gained, " Health!", sep='')
        print("")

        self.mainGameStart()

    def lose(self):
        print("You lost! Thanks for trying! - Trev")

    def fightLoop(self, pHand, oDeck, oHand, oHealth):
        pHand.append(self.playerDeck.drawCard())
        oHand.append(oDeck.drawCard())

        print("Your health: ", self.health, '/', self.healthMax, sep='')
        print("Opponent health: ", oHealth, sep='')

        for x in range(0, len(pHand)):
            print(pHand[x].getGameCard(), end=' ')

        print("")

        while True:
            decision = input('')
            if(decision not in ('S', 's')):
                try:
                    print('You selected:', pHand[int(decision)-1].getGameCard())
                    uChoice = pHand[int(decision)-1]
                    pHand.pop(int(decision)-1)
                    break
                except (ValueError, IndexError):
                    print("Try that again!")
            else:
                print('You shuffled!')
                pHand = self.newHand()
                uChoice = pHand[-1]
                pHand.pop(-1)
                break

        opChoice, indic = self.pickCard(oHand)
        print('They selected:', opChoice.getGameCard())
        print('')
        oHand.pop(indic)

        if(uChoice > opChoice):
            diff = uChoice.number - opChoice.number 
            print(diff, " damage done.", sep='')
            oHealth = oHealth - diff

        elif(uChoice == opChoice):
            print("Draw.")

        else:
            diff = opChoice.number - uChoice.number
            print( diff, " damage done to you. Health:", self.health - diff, sep='')
            self.health = self.health - diff

        if(oHealth <= 0):
            print("You won! You can now steal a card from cards that your opponent dropped as the legged it!")
            toChoose = []

            for x in range(0, 3):
                toChoose.append(oDeck.drawCard())
                print(toChoose[x].getGameCard(), end=' ')
            
            print('')
            a = input("Which would you like? ")
            self.playerDeck.addCard(toChoose[int(a) - 1])
            self.mainGameStart()

        elif(self.health <= 0):
            self.lose()
        else:
            self.fightLoop(pHand, oDeck, oHand, oHealth)

    def fightSetup(self): 
        opponentDeck = deck(self.Jokers)
        playerHand = []
        opponentHand = []
        opponentHealth = random.randint(1, 10)

        print("You bumped into someone! It's time to fight!")
        
        for x in range(0, 4):
            playerHand.append(self.playerDeck.drawCard())
            opponentHand.append(opponentDeck.drawCard())

        self.fightLoop(playerHand, opponentDeck, opponentHand, opponentHealth)
        
    def mainGameStart(self):
        options = self.generateOptions()
        print("You continue along the endless road.")
        print("You can either look at your deck (D) or you can take one of the", len(options),  "options ahead of you. They are as follows:")
        for x in range(len(options)):
            print(x+1, ':[', options[x], ']  ', sep='', end='')
        
        print("")
        
        choice = input("Select which option you'd like to explore! ")
        try:
            if(choice == 'D'):
                self.playerDeck.printDeck()
                print('')
                self.mainGameStart()
            elif(options[int(choice) - 1] == 'X'):
                self.fightSetup()
            elif(options[int(choice) - 1] == 'F'):
                self.fire()
            else:
                print("Oops! It seems something went wrong. You look around again and find yourself in unfamiliar territory.")
                self.mainGameStart()
        except (ValueError, IndexError):
            print("Oops! It seems something went wrong. You look around again and find yourself in unfamiliar territory.")
            self.mainGameStart()


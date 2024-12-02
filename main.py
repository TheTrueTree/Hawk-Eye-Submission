from gameSegments import *

Jokers = False

def setOptions():
    global Jokers
    print("Select which option to change!")
    print("[1] - Jokers", end='')

    if(Jokers):
        print(" = True")
    else:
        print(" = False")

    print("[2] - Back to menu")
    x = input('')

    if(str(x) == '1'):
        Jokers = not Jokers
        setOptions()
    else:
        start()

def start():
    global Jokers
    print("Welcome to Higher!")
    print("[1] - Play")
    print("[2] - Play (No tutorial)")
    print('[3] - Options')
    
    option = input('')
    if(str(option) == '1'):
        game = Game(Jokers)
        game.tutorial()

    elif(str(option) == '2'):
        game = Game(Jokers)
        game.mainGameStart()
    
    else:
        setOptions()

start()

#Naughts And Crosses Game By Spike 2019


from Gridrender import p1check
from Gridrender import p2check

print("\nNOUGHTS & CROSSES!")
print("\n    /    /    ")
print("    /    /    ")
print("    /    /    ")
print("--------------")
print("    /    /    ")
print("    /    /    ")
print("    /    /    ")
print("--------------")
print("    /    /    ")
print("    /    /    ")
print("    /    /    ")

CounterSet = False

while CounterSet == False:
    Player1Counter = input("\nPlayer 1, O or X? ")
    if Player1Counter == "o":
        Player1Counter = "O"
    if Player1Counter == "x":
        Player1Counter = "X"
    if Player1Counter == "O":
        print("You have chosen " + Player1Counter + "'s!")
        CounterSet = True
    elif Player1Counter == "X":
        print("You have chosen " + Player1Counter + "'s!")
        CounterSet = True


    else:
        print("Sorry, that's not an option, you must type \"O\" or \"X\"")


if Player1Counter == "O":
    Player2Counter = "X"
if Player1Counter == "X":
    Player2Counter = "O"

print("That means you are " + Player2Counter + "'s, Player 2!")
input()
print("The rules are simple; Take it in turns to place your X or O, simply by \nentering the number of the square you wish to occupy and pressing enter.")

print("\nReady?!")
input("Press any key to continue\n")


# All the default strings of the Grid

#Empty squares TB = TopBottom
# Default Strings
TB = "    /"
End = "    \n"
Centre1 = "  1 /"
Centre2 = "  2 /"
Centre3 = "  3 \n"
Centre4 = "  4 /"
Centre5 = "  5 /"
Centre6 = "  6 \n"
Centre7 = "  7 /"
Centre8 = "  8 /"
Centre9 = "  9 \n"
Divide = "--------------\n"

# X replacement Strings
XTB = "X  X/"
XEnd = "X  X\n"
XCen = " XX /"
XEndCen = " XX \n"

# O replacement Strings
OTB = " OO /"
OEnd = " OO \n"
OCen = "O  O/"
OEndCen = "O  O\n"

Line1 = TB + TB + End
Line2 = Centre1 + Centre2 + Centre3
Line3 = TB + TB + End
Line4 = TB + TB + End
Line5 = Centre4 + Centre5 + Centre6
Line6 = TB + TB + End
Line7 = TB + TB + End
Line8 = Centre7 + Centre8 + Centre9
Line9 = TB + TB + End

Grid = "\n" + Line1 + Line2 + Line3 + Divide + Line4 + Line5 + Line6 + Divide + Line7 + Line8 + Line9

print(Grid)


# P1 Choosing a number to place counter on, checking to see if they have won, and Swapping turn
Win = False
PlayerTurn = "1"
Player1Occupied = []
Selection = []
Turn = 0
print(Turn)
Winner = "0"
WinMessage = "Congratulations, Player " + Winner + "! You Win!"
Player2Occupied = []

def p1win():
    Win = True
    Winner = "1"
    print(WinMessage)
    return 3

def p2win():
    Win = True
    Winner = "2"
    print(WinMessage)
    return 4

#Checks all winning combinations against owned squares
def p1wincheck():
    if ["1", "2", "3"] in Player1Occupied:
        p1win()
    if ["4", "5", "6"] in Player1Occupied:
        p1win()
    if ["7", "8", "9"] in Player1Occupied:
        p1win()
    if ["1", "4", "7"] in Player1Occupied:
        p1win()
    if ["2", "5", "8"] in Player1Occupied:
        p1win()
    if ["3", "6", "9"] in Player1Occupied:
        p1win()
    if ["1", "5", "9"] in Player1Occupied:
        p1win()
    if ["3", "5", "7"] in Player1Occupied:
        p1win()



def p2wincheck():
    if ["1", "2", "3"] in Player2Occupied:
        p2win()
    if ["4", "5", "6"] in Player2Occupied:
        p2win()
    if ["7", "8", "9"] in Player2Occupied:
        p2win()
    if ["1", "4", "7"] in Player2Occupied:
        p2win()
    if ["2", "5", "8"] in Player2Occupied:
        p2win()
    if ["3", "6", "9"] in Player2Occupied:
        p2win()
    if ["1", "5", "9"] in Player2Occupied:
        p2win()
    if ["3", "5", "7"] in Player2Occupied:
        p2win()



Squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while Win == False:
    while PlayerTurn == "1":
        Selection = input("Player " + PlayerTurn + " Choose a Square...")
        if Selection in Squares and Selection not in Player2Occupied:
            Player1Occupied.insert(0 + Turn, Selection)
            p1check()
            p1wincheck()
            Turn = Turn + 1
            PlayerTurn = "2"
            print(Grid)
            continue
        else:
            print("Sorry, that is not a valid selection, please choose a free number from 1-9 and press enter")

print(Player1Occupied)

    # P2 Choosing a number to place counter on and Swapping turn

Selection = []
while PlayerTurn == "2":
    Selection = input(" Player " + PlayerTurn + " Choose a Square... ")
    if Selection in Squares and Selection not in Player1Occupied:
        Player2Occupied.insert(0 + Turn, Selection)
        p2check()
        p2wincheck()
        Turn + 1
        PlayerTurn = "1"
        print(Grid)
    else:
        print("Sorry, that is not a valid selection, please choose a number from 1-9 and press enter")

print(Player2Occupied)


input()
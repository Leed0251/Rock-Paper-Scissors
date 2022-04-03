from msilib import Table
import random
import math
import os

# finds the most frequently chosen object
# limit of six (set in computer choice function)
def getMostFrequentValue(list):
    valfrequency = []
    
    for i in range(0,len(list)):
        found = False
        for v in range(0,len(valfrequency)):
            if list[v][0] == i:
                list[v][1] = list[v][1] + 1
                found = True
        if found == False:
            valfrequency.append([list[i],1])
    value = ""
    valuenumber = 0
    for i in range(0,len(valfrequency)):
        if valuenumber < valfrequency[i][1]:
            value = valfrequency[i][0]
            valuenumber = valfrequency[i][1]
    return value

# Clears the console output
def clearConsole():
    command = "clear"
    if os.name in ("nt","dos"):
        command = "cls"
    os.system(command) # Runs the clear command

def ComputerChoice():
    return GetChoice(random.choice(wins)[0])

def GetChoice(choice):
    choice = choice.lower()
    if choice:
        for i in range(len(wins)):
            if choice == wins[i][0][0:len(choice)]:
                return wins[i]
            if choice == "xxx":
                return "xxx"
        return False

def GetWinner(user,computer):
    print("""
    \x1B[90mComputer picked: \x1B[1m{}\x1B[0m
    \x1B[36mPlayer picked: \x1B[1m{}\x1B[0m
    """.format(computer[0],user[0])) # Prints the choices
    for i in range(len(wins)):
        if computer[1] == user[0]:
            return computer[0]
        elif computer[0] == user[1]:
            return user[0]
        elif computer == user:
            return False

def GetInput(player):
    error = 'That is not a choice'
    try:
        print('\x1B[0mPlease pick \x1B[90mrock\x1B[0m / \x1B[97mpaper\x1B[0m / \x1B[37mscissors\x1B[0m\x1B[0m or type \x1B[1m\x1B[91m"xxx"\x1B[0m to leave \x1B[3m')
        user = GetChoice(input(player))
        if user:
            return user
        else:
            print(error)
            return GetInput(player)
    except:
        print(error)
        return GetInput(player)

def RoundsToPlay():
    try:
        Number = input("""How many rounds would you like to play? \x1B[90m\x1B[3m0 for Infinite\x1B[0m 
""")
        if Number == "":
            return 0
        return int(Number)
    except:
        print("\x1B[31mPlease pick a number\x1B[0m")
        return RoundsToPlay()


def MainGame(mode):
    repeat = ""

    wins = 0
    ties = 0
    loses = 0
    roundsplayed = 0

    global total_wins
    global total_ties
    global total_loses
    global total_rounds

    global total_wins_multi
    global total_ties_multi
    global total_loses_multi
    global total_rounds_multi

    infinite = False
    roundstoplay = RoundsToPlay()
    clearConsole()
    if roundstoplay == 0:
        infinite = True
        print("""
\x1B[3mplaying INFINITE
        \x1B[0m""")
    user = ""
    computer = ""

    while user != "xxx" and computer != "xxx":
        if infinite == True:
            roundstoplay += 1
        if roundsplayed > roundstoplay-1:
            user = "xxx"
        else:
            if infinite == True:
                print("\x1B[1m----- \x1B[92mROUND \x1B[32m{}\x1B[0m\x1B[1m -----\x1B[0m".format(roundsplayed+1))
            else:
                print("\x1B[1m----- \x1B[92mROUND \x1B[32m{} / {}\x1B[0m\x1B[1m -----\x1B[0m".format(roundsplayed+1,roundstoplay))
            user = GetInput("Player 1: ")
            if user != "xxx":
                if mode == "Single":
                    computer = ComputerChoice()
                elif mode == "Multi":
                    clearConsole()
                    computer = GetInput("Player 2: ")
        if user != "xxx" and computer != "xxx":
            clearConsole()
            winner = GetWinner(user,computer)
            roundsplayed += 1
            if mode == "Single":
                total_rounds += 1
            elif mode == "Multi":
                total_rounds_multi += 1
            if winner == user[0]: # Prints who won
                print("\x1B[32mWinner: \x1B[1mPlayer\x1B[0m\n")
                wins += 1
                if mode == "Single":
                    total_wins += 1
                elif mode == "Multi":
                    total_wins_multi += 1
            elif winner != user[0] and winner != False:
                print("\x1B[31mWinner: \x1B[1mComputer\x1B[0m\n")
                loses += 1
                if mode == "Single":
                    total_loses += 1
                elif mode == "Multi":
                    total_loses_multi += 1
            else:
                print("\x1B[33m\x1B[1mTied\x1B[0m\n")
                ties += 1
                if mode == "Single":
                    total_ties += 1
                elif mode == "Multi":
                    total_ties_multi += 1
    input("""\x1B[1m
\x1B[32mWins: {} 
\x1B[33mTies: {} 
\x1B[31mLoses: {}\x1B[90m\x1B[3m
Press <enter> to continue\x1B[0m""".format(wins,ties,loses))
    clearConsole()
    Play()

def Play():
    game = input("""
What would you like to play?
\x1B[32mAvailable modes:\x1B[90m\x1B[3m
    singleplayer
    multiplayer
    \x1B[0m
    You can type \x1B[31m"quit"\x1B[0m to quit
""")
    clearConsole()
    if game.lower() != "":
        if game.lower() == "singleplayer"[0:len(game)]:
            MainGame("Single")
        elif game.lower() == "multiplayer"[0:len(game)]:
            MainGame("Multi")
        elif game.lower() == "quit":
            confirmation = input("""Are you sure you want to quit?
""")
            if confirmation.lower() == "yes"[0:len(confirmation)]:
                print("""
    \x1B[31mQuit game\x1B[0m""")
            else:
                clearConsole()
                Play()
        else:
            print('"{}" is not an option'.format(game))
            Play()
    else:
        print("Please type something")
        Play()


# ***** MAIN ROUTINE STARTS HERE ******
wins = [
    ["rock","scissors"],
    ["paper","rock"],
    ["scissors","paper"]
]

total_wins = 0
total_ties = 0
total_loses = 0

total_wins_multi = 0
total_ties_multi = 0
total_loses_multi = 0

total_rounds = 0
total_rounds_multi = 0

clearConsole() # Clears any visible code while starting up
Play()
clearConsole()

# Displays the users stats
print("\x1B[1m******* COMPLETE SUMMARY *******\x1B[0m")
if total_rounds > 0:
    accuracy = math.ceil(((total_wins+(total_ties/2))/total_rounds) * 100)
    print("""
******* SINGLE PLAYER *******
    \x1B[32mTotal Wins: {} 
    \x1B[33mTotal Ties: {} 
    \x1B[31mTotal Loses: {}

\x1B[97mAccuracy: {}%
Total Rounds: {}""".format(total_wins,total_ties,total_loses,accuracy,total_rounds))

if total_rounds_multi > 0:
    accuracy_multi = math.ceil(((total_wins_multi+(total_ties_multi/2))/total_rounds_multi) * 100)
    print("""\x1B[0m
******* MULTIPLAYER *******
    \x1B[32mTotal Wins: {} 
    \x1B[33mTotal Ties: {} 
    \x1B[31mTotal Loses: {}

\x1B[97mAccuracy: {}%
Total Rounds: {}
    """.format(total_wins_multi,total_ties_multi,total_loses_multi,accuracy_multi,total_rounds_multi))

input("\x1B[90m\x1B[3mPress <enter> to close\x1B[0m")

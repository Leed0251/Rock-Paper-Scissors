from msilib import Table
import random

wins = [
    ["rock","scissors"],
    ["paper","rock"],
    ["scissors","paper"]
]

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



userInputHistory = []

def GetOpposingChoice(choice):
    for i in range(0,len(wins)):
        if wins[i][1] == choice:
            return GetChoice(wins[i][0])

def ComputerChoice():
    if len(userInputHistory) >= 1:
        if len(userInputHistory) >= 6:
            userInputHistory.pop(0)
        frequent = getMostFrequentValue(userInputHistory)
        num = random.randrange(1,4)
        if num == 1:
            return GetOpposingChoice(frequent)
        else:
            return GetChoice(random.choice(wins)[0])
    else:
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

def GetInput():
    error = 'That is not a choice'
    try:
        user = GetChoice(input('\x1B[0mPlease pick \x1B[90mrock\x1B[0m / \x1B[97mpaper\x1B[0m / \x1B[37mscissors\x1B[0m\x1B[0m or type \x1B[1m\x1B[91m"xxx"\x1B[0m to leave \x1B[3m'))
        if user:
            return user
        else:
            print(error)
            return GetInput()
    except:
        print(error)
        return GetInput()

def Infinite():
    repeat = ""
    wins = 0
    ties = 0
    loses = 0
    roundsplayed = 0
    user = ""

    while not user == "xxx":
        computer = ComputerChoice()
        print("\x1B[1m----- \x1B[92mROUND \x1B[32m{}\x1B[0m\x1B[1m -----\x1B[0m".format(roundsplayed+1))
        user = GetInput()
        if user != "xxx":
            winner = GetWinner(user,computer)

            userInputHistory.append(user[0])
            roundsplayed += 1
            if winner == user[0]: # Prints who won
                print("\x1B[32mWinner: \x1B[1mPlayer\x1B[0m\n")
                wins += 1
            elif winner != user[0] and winner != False:
                print("\x1B[31mWinner: \x1B[1mComputer\x1B[0m\n")
                loses += 1
            else:
                print("\x1B[33m\x1B[1mTied\x1B[0m\n")
                ties += 1
    print("""\x1B[1m
\x1B[32mWins: {} 
\x1B[33mTies: {} 
\x1B[31mLoses: {}\x1B[0m""".format(wins,ties,loses))
    Play()

def Continuous():
    repeat = ""
    wins = 0
    ties = 0
    loses = 0
    roundsplayed = 0
    roundstoplay = int(input("How many rounds would you like to play? "))
    user = ""

    while not user == "xxx":
        computer = ComputerChoice()
        if roundsplayed > roundstoplay-1:
            user = "xxx"
        else:
            print("\x1B[1m----- \x1B[92mROUND \x1B[32m{} / {}\x1B[0m\x1B[1m -----\x1B[0m".format(roundsplayed+1,roundstoplay))
            user = GetInput()
        if user != "xxx":
            winner = GetWinner(user,computer)

            userInputHistory.append(user[0])
            roundsplayed += 1
            if winner == user[0]: # Prints who won
                print("\x1B[32mWinner: \x1B[1mPlayer\x1B[0m\n")
                wins += 1
            elif winner != user[0] and winner != False:
                print("\x1B[31mWinner: \x1B[1mComputer\x1B[0m\n")
                loses += 1
            else:
                print("\x1B[33m\x1B[1mTied\x1B[0m\n")
                ties += 1
    input("""\x1B[1m
\x1B[32mWins: {} 
\x1B[33mTies: {} 
\x1B[31mLoses: {}\x1B[90m\x1B[3m
Press <enter> to continue\x1B[0m""".format(wins,ties,loses))
    Play()

def Play():
    game = input("""
What would you like to play?
\x1B[32mAvailable modes:\x1B[90m\x1B[3m
    continuous
    infinite
    \x1B[0m
    You can type \x1B[31m"quit"\x1B[0m to quit
""")
    if game.lower() == "infinite":
        Infinite()
    if game.lower() == "continuous":
        Continuous()
    elif game.lower() == "quit":
        print("""
\x1B[31mQuit game\x1B[0m""")
    else:
        print("That is not a choice")
        Play()
Play()
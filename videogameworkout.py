import random
workouts = ["Pushups", "Goblet Squats", "Kettlebell Swings", "Bicycles"]

def rlworkout():
    gameInfo = {}
    gameInfo['myScore'] = int(input("How many goals did your team score? "))
    gameInfo['opponentScore'] = int(input("How many goals did the other team score? "))
    gameInfo['goals'] = int(input("How many goals did you score? "))
    gameInfo['assist'] = int(input("How many assists did you make? "))
    gameInfo['saves'] = int(input("How many goals did you save? "))
    
    if gameInfo['myScore'] >= 0 and gameInfo['opponentScore'] >= 0:
        if gameInfo['myScore'] > gameInfo['opponentScore']:
            determineRocketLeagueWin(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
            for k, v in gameInfo.items():
                print(k, ':', v)
            
        else:
            determineRocketLeagueLoss(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
            for k, v in gameInfo.items():
                print(k, ':', v)
    else:
        print("Doesn't make sense dude")


def owworkout():
    gameInfo = {}
    gameInfo['result'] = input("Did you win or lose? ")
    gameInfo['kills'] = int(input("How many kills did you get? "))
    gameInfo['deaths'] = int(input("How many times did you get killed? "))
    gameInfo['healing'] = int(input("How much healing did you do? "))
    
    if gameInfo['result'] == "Win" or gameInfo['result'] == "win":
        determineOverwatchWin(gameInfo['kills'], gameInfo['deaths'], gameInfo['healing'])
    elif gameInfo['result'] == "Lost" or gameInfo['result'] == "lost":
        determineOverwatchLoss(gameInfo['kills'], gameInfo['deaths'], gameInfo['healing'])
    else:
        print("That's not what I asked bitch!")

def determineRocketLeagueLoss(goals, assist, saves):
    print("You lost, womp")
    workout = random.choice(workouts)
    amount = int(round((25 - (goals * 2) - assist - saves)))
    print('Do', amount, workout)

def determineRocketLeagueWin(goals, assist, saves):
    print("You won!")
    workout = random.choice(workouts)
    amount = 5
    print('Do', amount, workout)

def determineOverwatchWin(kills, deaths, healing):
    print("You won!")
    workout = random.choice(workouts)
    amount = 5
    print('Do', amount, workout)

def determineOverwatchLoss(kills, deaths, healing):
    print("You lost, womp")
    workout = random.choice(workouts)
    amount = int(round(15 - kills + deaths - (healing * .001)))
    print('Do', amount, workout)
    print(healing * .001)

def collectInfo():
    gameInfo = {}
    gameInfo['myScore'] = int(input("How many goals did your team score?"))
    gameInfo['opponentScore'] = int(input("How many goals did the other team score?"))
    gameInfo['goals'] = int(input("How many goals did you score?"))
    gameInfo['assist'] = int(input("How many assists did you make?"))
    gameInfo['saves'] = int(input("How many goals did you save?"))
    return gameInfo

    

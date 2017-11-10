import random
workouts = ["Pushups", "Goblet Squats", "Kettlebell Swings", "Bicycles", "Shoulder Press", "Ab Roller", "Bicep Curls", "Tricep Extensions", "Bent Rows", "Shoulder Raises"]

def main():
    game_played = str(input("What game did you play? "))
    game_played.lower()
    if game_played == "overwatch":
        owworkout()
    elif game_played =="rocket league":
        rlworkout()
    else:
        print("That isn't supported")
        
def rlworkout():
    gameInfo = getInfoRL()
    
    if gameInfo['myScore'] >= 0 and gameInfo['opponentScore'] >= 0:
        if gameInfo['myScore'] > gameInfo['opponentScore']:
            determineRocketLeagueWin(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
        else:
            determineRocketLeagueLoss(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
    else:
        print("Doesn't make sense dude")

    printStats(gameInfo)
    savegamedata(gameInfo)

    
def owworkout():
    gameInfo = getInfoOW()
    
    if gameInfo['result'] == "w":
        determineOverwatchWin(gameInfo['kills'], gameInfo['deaths'], gameInfo['healing'])
    elif gameInfo['result'] == "l":
        determineOverwatchLoss(gameInfo['kills'], gameInfo['deaths'], gameInfo['healing'])
    else:
        print("That's not what I asked bitch!")

    printStats(gameInfo)
    savegamedata(gameInfo)

def determineRocketLeagueLoss(goals, assist, saves):
    print("You lost, womp")
    workout = random.choice(workouts)
    amount = int(round((20 - (goals * 2) - assist - saves)))
    print('Do', amount, workout)

def determineRocketLeagueWin(goals, assist, saves):
    print("You won!")
    workout = random.choice(workouts)
    amount = random.randint(1, 10)
    print('Do', amount, workout)

def determineOverwatchWin(kills, deaths, healing):
    print("You won!")
    workout = random.choice(workouts)
    amount = random.randint(1, 10)
    print('Do', amount, workout)
 
def determineOverwatchLoss(kills, deaths, healing):
    print("You lost, womp")
    workout_tracker = {}
    workout = random.choice(workouts)
    amount = int(round(20 - kills + deaths - (healing * .001)))
    print('Do', amount, workout)
    workout_tracker[workout] = amount
    

def getInfoRL():
    gameInfo = {}
    gameInfo['myScore'] = int(input("How many goals did your team score? "))
    gameInfo['opponentScore'] = int(input("How many goals did the other team score? "))
    gameInfo['goals'] = int(input("How many goals did you score? "))
    gameInfo['assist'] = int(input("How many assists did you make? "))
    gameInfo['saves'] = int(input("How many goals did you save? "))
    return gameInfo
    

def getInfoOW():
    gameInfo = {}
    gameInfo['format'] = '-------'
    gameInfo['result'] = input("Did you win(w) or lose(l)? ")
    gameInfo['kills'] = int(input("How many kills did you get? "))
    gameInfo['deaths'] = int(input("How many times did you get killed? "))
    gameInfo['healing'] = int(input("How much healing did you do? "))
    return gameInfo
    

def printStats(game):
    for k, v in game.items():
        print(k, ' :', v)

def savegamedata(gameInfo):
    dict_print = gameInfo
    game_stats = open('game_stats.txt', 'a')
    for k, v in dict_print.items():
        game_stats.write('\n' + str(k) + ' :' + str(v))
    game_stats.close()

def saveworkoutdata(workout_tracker):
    workout_log = open('workout_log.txt', 'a')
    for k, v in workout_log.items():
        game_stats.write('\n' + str(k) + ' :' + str(v))
    workout_log.close()     
    
main()

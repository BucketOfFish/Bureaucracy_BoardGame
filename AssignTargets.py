import os
from numpy.random import randint

def pickOne(pool):
    nAvailable = len(pool)
    i = randint(nAvailable)
    toReturn = pool[i]
    pool.pop(i)
    return toReturn

def replaceAndPickAgain(pool, item):
    pool.append(item)
    nAvailable = len(pool)
    i = randint(nAvailable)
    toReturn = pool[i]
    pool.pop(i)
    return toReturn

def assignTargets():

    os.system('clear')

    players = []
    print "--------------------"
    print "Players are:"
    for player in open("Players.txt"):
        player = player.strip()
        players.append(player)
        print player
    print "--------------------"
    raw_input("Press any key to continue.")
    nPlayers = len(players)

    stillTargeting = True
    while stillTargeting:

        availableTargets = players + players
        targets = {}
        for player in players:

            loopedN = 0
            firstTarget = pickOne(availableTargets)
            while firstTarget == player:
                firstTarget = replaceAndPickAgain(availableTargets, firstTarget)
                loopedN += 1
                if loopedN > 10:
                    availableTargets.append(firstTarget)
                    break

            loopedN = 0
            secondTarget = pickOne(availableTargets)
            while secondTarget == player or secondTarget == firstTarget:
                secondTarget = replaceAndPickAgain(availableTargets, secondTarget)
                loopedN += 1
                if loopedN > 10:
                    availableTargets.append(secondTarget)
                    break

            targets[player] = [firstTarget, secondTarget]

        if len(availableTargets) == 0:
            stillTargeting = False

    for player in players:
        os.system('clear')
        print "Give the computer to", player
        raw_input("Once " + player + " has the computer, press any key to continue.")
        os.system('clear')
        print player + ", your targets are", targets[player][0], "and", targets[player][1]
        raw_input("Press any key to continue.")

    for player in players:
        print player+"'s Targets:", targets[player][0], "and", targets[player][1]
    os.system('clear')
    print "All targets assigned."

if __name__ == "__main__":
    assignTargets()

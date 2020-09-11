import bsClasses as bsc
import bsFuncs as bsf
import numpy as ny

print("Hello! Welcome to Battleship!")
allShips = bsf.makeAllShipGrid()
turn = 0
while (len(allShips.ships) > 0):
    foundS = False
    hit = [0, 0]
    while foundS == False:
        allShips, foundS, hit[0], hit[1] = bsf.search(allShips)
        turn += 1
    sunk = False
    while sunk == False:
        huntShips = allShips.huntGridOn(hit[0], hit[1])
        huntShips,allShips,sunk = bsf.hunt(huntShips, allShips)
        turn += 1
print("I've Won!")
print("It took " + str(turn) + " turns")

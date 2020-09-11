import bsClasses as bsc
import bsFuncs as bsf
import numpy as ny

print("Hello! Welcome to Battleship!")
allShips = bsf.makeAllShipGrid()
while (len(allShips.ships) > 0):
    foundS = False
    hit = [0, 0]
    while foundS == False:
        allShips, foundS, hit[0], hit[1] = bsf.search(allShips)
    sunk = False
    while sunk == False:
        huntShips = allShips.huntGridOn(hit[0], hit[1])
        huntShips,allShips,sunk = bsf.hunt(huntShips, allShips)
print("I've Won!")

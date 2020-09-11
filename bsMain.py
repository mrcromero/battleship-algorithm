import bsClasses as bsc
import bsFuncs as bsf
import numpy as ny

print("Hello! Welcome to Battleship!")
allShips = bsf.makeAllShipGrid()
turn = 0
# Loops until all ships have been found
while (len(allShips.ships) > 0):
    foundS = False # The flag for the search loop
    hit = [0, 0] # The hit while searching
    # Search until a hit is found
    while foundS == False:
        allShips, foundS, hit[0], hit[1] = bsf.search(allShips)
        turn += 1
    sunk = False # Flag for hunt loop
    # New hunting grid on the hit
    huntShips = allShips.huntGridOn(hit[0], hit[1])
    # Hunt until a ship has been sunk
    while sunk == False:
        huntShips,allShips,sunk = bsf.hunt(huntShips, allShips)
        turn += 1
print("I've Won!")
print("It took " + str(turn) + " turns")

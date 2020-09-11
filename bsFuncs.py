import bsClasses as bsc
import numpy as ny

def makeAllShipGrid():
# Function to return and make the beginning grid with all possible ship placements
    shipSizes = [2, 3, 3, 4, 5] # Different ship sizes
    shipList = [] # Will hold all ships
    matRep = ny.zeros((10, 10)) # The matrix rep of the grid

    # Ships that go right/down go in P; ships that go left/up go in N
    shipsFitP = {}
    shipsFitN = {}

    # Figuring out which ship sizes fit in which values. Whichever ships fit
    # going up/down will fit going left/right respectively
    for i in range(10):
        shipsFitP[i] = []
        shipsFitN[i] = []
        for size in shipSizes:
            if (i + 1 - size) > -1:
                shipsFitN[i].append(size)
            if (i - 1 + size) < 10:
                shipsFitP[i].append(size)

    # Populating matRep and shipList. Works by making the ships that fit at
    # each point on the grid and then adds them to matRep and shipList
    for row in range(10):
        for col in range(10):
            # All the lengths that fit up, down, left, and right at the point
            shipsDown = shipsFitP[row]
            shipsUp = shipsFitN[row]
            shipsLeft = shipsFitN[col]
            shipsRight = shipsFitP[col]

            # Loops go through the ship lengths that fit in every direction.
            # Makes the ships of each viable size and appends them to the
            # shipList and adds them to the matrix representation
            for len in shipsDown:
                points = [] # Will hold the points that the ship is on
                shipMat = ny.zeros((10, 10)) # The points in a matrix
                # loop through different row vals that ship is on. Cols stay
                # the same. Add each pt to the list and the matrix
                for i in range(row, row+len):
                    points.append((i, col))
                    shipMat[i, col] = 1
                # Make a ship object and add them and their matrix rep to
                # shipList and matRep respectively.
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

            for len in shipsRight:
            # Same as before but loop through columns going right
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(col, col+len):
                    points.append((row, i))
                    shipMat[row, i] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

            for len in shipsUp:
            # Loops through rows going up
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(row-len+1, row+1):
                    points.append((i, col))
                    shipMat[i, col] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

            for len in shipsLeft:
            # Loops through columns going left
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(col-len+1, col+1):
                    points.append((row, i))
                    shipMat[row, i] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

    return bsc.Grid(shipList, [], matRep)

def search(allShips):
# Search algorithm and querying the user
    hit = False
    # get an attack
    atkR,atkC = allShips.getAtk()
    print("I attack at row " + str(atkR+1) + " and column " + str(atkC+1))
    answer = input("Did my attack hit? (Y/n) ")
    while (answer != "Y" and answer != "n"):
        print("Sorry, I didn't get that")
        answer = input("Did my attack hit? (Y/n) ")
    # Perform hitOn or missOn as appropriate
    if (answer == "Y"):
        print("Nice")
        # turn hit to true on a hit
        hit = True
        allShips.hitOn(atkR,atkC)
    elif (answer == "n"):
        print("Aww man")
        allShips.missOn(atkR, atkC)
    return allShips,hit,atkR,atkC

def hunt(huntShips, allShips):
# Hunt algorithm and querying the user
    sunk = False
    atkR,atkC = huntShips.getAtk()
    print("I attack at row " + str(atkR+1) + " and column " + str(atkC+1))
    answer = input("Did my attack hit? (Y/n) ")
    while (answer != "Y" and answer != "n"):
        print("Sorry, I didn't get that")
        answer = input("Did my attack hit? (Y/n) ")
    if (answer == "Y"):
        print("Nice")
        # On hits, perform hit on for both Grids so when hunting is done, the
        # hits are preserved on the alShips grid.
        allShips.hitOn(atkR,atkC)
        huntShips.hitOn(atkR,atkC)
        # Ask if ship hit. A sink ends the loop for the hunting algorithm
        answerS = input("Did I sink a ship? (Y/n) ")
        while (answerS == "Y" and answerS == "n"):
            print("Sorry, I didn't get that")
            answerS = input("Did I sink a ship? (Y/n) ")
        if (answerS == "Y"):
            # Assumes that the user inputs the correct size.
            sinkSz = int(input("What size? "))
            allShips.sunk(sinkSz)
            sunk = True
    elif (answer == "n"):
        # On miss, only perform missOn for both Grids so when hunting is done,
        # the misses are preserved.
        print("Aww man")
        allShips.missOn(atkR, atkC)
        huntShips.missOn(atkR, atkC)
    return huntShips,allShips,sunk

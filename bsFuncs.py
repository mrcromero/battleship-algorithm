import bsClasses as bsc
import numpy as ny

def makeAllShipGrid():
# Function to make the beginning grid with all possible ship placements
    shipSizes = [2, 3, 3, 4, 5]
    shipList = []
    matRep = ny.zeros((10, 10))

    # Ships that go right/down go in P; ships that go left/up go in N
    shipsFitP = {}
    shipsFitN = {}

    # Figuring out which ship sizes fit in which points
    for i in range(10):
        shipsFitP[i] = []
        shipsFitN[i] = []
        for size in shipSizes:
            if (i + 1 - size) > -1:
                shipsFitN[i].append(size)
            if (i - 1 + size) < 10:
                shipsFitP[i].append(size)

    # Populating matRep and shipList
    for row in range(10):
        for col in range(10):
            # All the lengths that fit up, down, left, and right at the point
            shipsDown = shipsFitP[row]
            shipsUp = shipsFitN[row]
            shipsLeft = shipsFitN[col]
            shipsRight = shipsFitP[col]

            for len in shipsDown:
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(row, row+len):
                    points.append((i, col))
                    shipMat[i, col] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

            for len in shipsRight:
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(col, col+len):
                    points.append((row, i))
                    shipMat[row, i] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

            for len in shipsUp:
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(row-len+1, row+1):
                    points.append((i, col))
                    shipMat[i, col] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat

            for len in shipsLeft:
                points = []
                shipMat = ny.zeros((10, 10))
                for i in range(col-len+1, col+1):
                    points.append((row, i))
                    shipMat[row, i] = 1
                ship = bsc.Ship(points, shipMat)
                shipList.append(ship)
                matRep += shipMat
    print(matRep)

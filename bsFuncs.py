import bsClasses as bsc
import numpy as ny

def makeAllShipGrid():
# Function to make the beginning grid with all possible ship placements
    shipSizes = [2, 3, 3, 4, 5]
    shipList = []
    matRep = ny.zeros((9, 9))

    # Ships that go right/down go in P; ships that go left/up go in N
    shipsFitP = {}
    shipsFitN = {}

    # Figuring out which ship sizes fit in which points
    for i in range(9):
        shipsFitP[i] = []
        shipsFitN[i] = []
        for size in shipSizes:
            if (i + 1 - size) > -1:
                shipsFitN[i].append(size)
            if (i - 1 + size) < 9:
                shipsFitP[i].append(size)

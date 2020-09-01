import bsClasses as bsc
import numpy as ny

def makeAllShipGrid():
# Function to make the beginning grid with all possible ship placements
    shipSizes = [2, 3, 3, 4, 5]
    shipList = []
    matRep = ny.zeros((9, 9))

    # Negative values go upwards/left, positive values downwards/right
    shipsFit = {}

    for i in range(9):
        shipsFit[i] = []
        for size in shipSizes:
            if (i + 1 - size) > -1:
                shipsFit[i].append(size * -1)
            if (i - 1 + size) < 9:
                shipsFit[i].append(size)

import numpy as ny

class Ship:
# Ship object
    def __init__(self, points, matrix_rep):
        self.length = len(points) # Length of the ship
        self.points = points # points that the ship is on
        self.mat = matrix_rep # the points in a matrix

    def search(self, ptR, ptC):
    # Determines if pt ptR, ptC hits the ship
        pt = ptR, ptC
        query = False
        if pt in self.points:
            query = True
        return query


class Grid:
    def __init__(self, ships, hits, matrix_rep):
        self.ships = ships # possible ship placements
        self.mat = matrix_rep # heatmap of the grid
        self.hits = hits # points on grid w/ hits. Only to pass to hunt grid
        self.rem = remShips # remaining ship sizes

    def missOn(self, ptR, ptC):
    # Course of action when position ptR, ptC misses
        ships = self.ships
        # Go through ships backwards so no index errors
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            # Any points on the miss get removed (no longer valid placements)
            if ship.search(ptR, ptC) == true:
                self.ships.pop((i))
                self.mat -= ship.mat
        return

    def hitOn(self, ptR, ptC):
    # Course of action when position ptR, ptC hits
        point = (ptR, ptC)
        self.hits.append(point)
         # Set to 0 (no longer valid attack point, but ships touching hit can
         # still exist as possible placements)
        self.mat[point] = 0
        return

    def huntGridOn(self, ptR, ptC):
    # On a first-time-hit, switch to hunt mode
        ships = self.ship
        hShips = []
        hMat = ny.zeros((9, 9))
        # All ships that touch the hit get added to the new hunt grid
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            if ship.search(ptR, ptC) == true:
                hShips.append(self.ships[i])
                shipMat = ship.mat
                hMat += ship.mat
        hits = self.hits
        # Pass through all hits and set them as 0
        for hit in hits:
            hMat[hit] = 0
        hunt = Grid(hShips, [], hMat) # Doesn't need to know hits or sizes
        return

    def sunk(self, sz):
    # Remove any other possible placements of size sz (size 3 ships only get
    # removed once)
        ships = self.ships
        rmShips = set() # use a set because doesn't allow for copies
        oldLen = len(rmShips)
        for i in range(len(ships)-1, -1, -1):
            ship = ship[i]
            # Add ships of length sz to rmShips. Only remove if unique ship.
            if ship.length == sz:
                rmShips.add(ship)
                newLen = len(rmShips)
                if oldLen != newLen:
                    oldLen = newLen
                    self.ships.pop((i))
                    self.mat -= ship.mat
        return

    def getAtk(self):
    # Find the most likely attack point
        max = ny.max(self.mat)
        indR, indC = ny.where(self.mat == max)
        size = indR.shape[0]
        atkR = 0
        atkC = 0
        # More than 1 possible attacks? Choose a random one.
        if size > 1:
            ptCh = ny.random.randint(size)
            atkR = indR[ptCh]
            atkC = indC[ptCh]
        else:
            atkR = indR[0]
            atkC = indC[0]
        return atkR,atkC

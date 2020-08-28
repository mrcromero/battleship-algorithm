import numpy as ny

class Ship:
    def __init__(self, points, matrix_rep):
        self.length = len(points)
        self.points = points
        self.mat = matrix_rep

    def search(self, ptR, ptC):
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

    def missOn(self, ptR, ptC):
        ships = self.ships
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            if ship.search(ptR, ptC) == true:
                self.ships.pop((i))
                self.mat -= ship.mat
        return

    def hitOn(self, ptR, ptC):
        point = (ptR, ptC)
        self.hits.append(point)
        self.mat[point] = 0
        return

    def huntGridOn(self, ptR, ptC):
        ships = self.ship
        hShips = []
        hMat = ny.zeros(9, 9)
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            if ship.search(ptR, ptC) == true:
                hShips = self.ships[i]
                shipMat = ship.mat
                hMat += ship.mat
        hits = self.hits
        for hit in hits:
            hMat[hit] = 0
        hunt = Grid(hShips, [], hMat) # Doesn't need to know hits
        return hunt

    def getAtk(self):
        max = ny.max(self.mat)
        indR, indC = ny.where(self.mat == max)
        size = indR.shape[0]
        atkR = 0
        atkC = 0
        if size > 1:
            ptCh = ny.random.randint(size)
            atkR = indR[ptCh]
            atkC = indC[ptCh]
        else:
            atkR = indR[0]
            atkC = indC[0]
        return atkR,atkC

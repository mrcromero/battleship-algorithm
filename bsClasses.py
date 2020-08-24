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
    def __init__(self, ships, matrix_rep):
        self.ships = ships
        self.mat = matrix_rep

    def shipsOnRem(self, ptR, ptC):
        ships = self.ships
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            if ship.search(ptR, ptC) == true:
                self.ships.pop((i))
                self.mat -= ship.mat
        return

    def shipsOffRem(self, ptR, ptC):
        ships = self.ships
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            if ship.search(ptR, ptC) == false:
                self.ships.pop((i))
                self.mat -= ship.mat
        return

    def huntGridOn(self, ptR, ptC):
        ships = self.ship
        hShips = []
        hMat = ny.zeros(9, 9)
        for i in range(len(ships)-1, -1, -1):
            ship = ships[i]
            if ship.search(ptR, ptC) == true:
                hShips = self.ships.pop((i))
                shipMat = ship.mat
                self.mat -= shipMat
                hMat += ship.mat
        hunt = Grid(hShips, hMat)
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

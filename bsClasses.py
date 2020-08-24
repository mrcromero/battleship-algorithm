import numpy as ny

class Ship:
    def __init__(self, points, matrix_rep):
        self.length = len(points)
        self.points = points
        self.mat = matrix_rep

    def search(self, ptR, ptC):
        pt = ptR, ptC
        query = False
        for point in self.points:
            if point == pt:
                query = True
                break
        return query

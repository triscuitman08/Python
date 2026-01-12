import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__xcoord = x
        self.__ycoord = y
        

    def getx(self):
        return self.__xcoord

    def gety(self):
        return self.__ycoord

    def distance_from_xy(self, x, y):
        return math.hypot(self.__xcoord - x, self.__ycoord - y)

    def distance_from_point(self, point):
        return math.hypot(self.__xcoord - point.getx(), self.__ycoord - point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__a = vertice1
        self.__b = vertice2
        self.__c = vertice3

    def perimeter(self):
        return (self.__a.distance_from_point(self.__b) +
                self.__b.distance_from_point(self.__c) +
                self.__c.distance_from_point(self.__a)
                )


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

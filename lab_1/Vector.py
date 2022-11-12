from Point import *


class Vector:
    _coordinates: Point

    def __init__(self, *args: Point):
        if len(args) == 1:
            if not isinstance(args[0], Point):
                raise TypeError("Argument must have argument of Point type")
            self._coordinates = Point(args[0].x, args[0].y)
        elif len(args) == 2:
            if not (isinstance(args[0], Point) and isinstance(args[1], Point)):
                raise TypeError("Argument ")
            self._coordinates = Point(args[1].x - args[0].x, args[1].y - args[0].y)
        else:
            raise AttributeError("Constructor of vector takes only 1 or 2 arguments of \'Point\' type")

    def __str__(self) -> str:
        return str(self._coordinates)

    def __add__(self, other):  # find info about set Vector as other type
        if not isinstance(other, Vector):
            raise TypeError("Argument must be instance of vector")
        return Point(self._coordinates.x + other._coordinates.x, self._coordinates.y + other._coordinates.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Argument must be instance of vector")
        return Point(self._coordinates.x - other._coordinates.x, self._coordinates.y - other._coordinates.y)

    def __mul__(self, other):
        if not isinstance(other, float):
            raise TypeError("Argument must be instance of float")
        return Point(self._coordinates.x * other, self._coordinates.y * other)

    def __invert__(self):
        return Point(-self._coordinates.x, -self._coordinates.y)

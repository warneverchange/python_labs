from Point2D import *
import math


class Vector2D:
    _coordinates: Point2D

    @property
    def x(self):
        return self._coordinates.x

    @x.setter
    def x(self, value):
        if not isinstance(value, Vector2D):
            raise TypeError("Argument must be an instance of Vector")
        self._coordinates.x = value

    @property
    def y(self):
        return self._coordinates.y

    @y.setter
    def y(self, value):
        if not isinstance(value, Vector2D):
            raise TypeError("Argument must be an instance of Vector")
        self._coordinates.y = value

    def __init__(self, *args: Point2D):
        if len(args) == 1:
            if not isinstance(args[0], Point2D):
                raise TypeError("Argument must have argument of Point type")
            self._coordinates = Point2D(args[0].x, args[0].y)
        elif len(args) == 2:
            if not (isinstance(args[0], Point2D) and isinstance(args[1], Point2D)):
                raise TypeError("Argument ")
            self._coordinates = Point2D(args[1].x - args[0].x, args[1].y - args[0].y)
        else:
            raise AttributeError("Constructor of vector takes only 1 or 2 arguments of \'Point\' type")

    def __str__(self) -> str:
        return f"{self._coordinates.x} * i + {self._coordinates.y} * j"

    def length(self) -> float:
        return math.sqrt(self._coordinates.x ** 2 + self._coordinates.y ** 2)

    def project(self, vector) -> float:
        if not isinstance(vector, Vector2D):
            raise TypeError("Argument must be instance of vector")
        return self.length() * math.cos(angel_between(self, vector))

    def dot_product(self, vector) -> float:
        if not isinstance(vector, Vector2D):
            raise TypeError("Argument must be instance of vector")
        return self.x * vector.x + self.y * vector.y

    def __add__(self, other) -> Point2D:  # find info about set Vector as other type
        if not isinstance(other, Vector2D):
            raise TypeError("Argument must be instance of vector")
        return Point2D(self._coordinates.x + other._coordinates.x, self._coordinates.y + other._coordinates.y)

    def __sub__(self, other) -> Point2D:
        if not isinstance(other, Vector2D):
            raise TypeError("Argument must be instance of vector")
        return Point2D(self._coordinates.x - other._coordinates.x, self._coordinates.y - other._coordinates.y)

    def __mul__(self, other) -> Point2D:
        if not isinstance(other, float):
            raise TypeError("Argument must be instance of float")
        return Point2D(self._coordinates.x * other, self._coordinates.y * other)

    def __invert__(self) -> Point2D:
        return Point2D(-self._coordinates.x, -self._coordinates.y)


def dot_product(v1: Vector2D, v2: Vector2D) -> float:
    if not (isinstance(v1, Vector2D) and isinstance(v2, Vector2D)):
        raise TypeError("Arguments must be an instance of Vector")
    return v1.dot_product(v2)


def angel_between(v1: Vector2D, v2: Vector2D) -> float:
    if not (isinstance(v1, Vector2D) and isinstance(v2, Vector2D)):
        raise TypeError("Arguments must be an instance of Vector")
    return math.acos(dot_product(v1, v2) / (v1.length() * v2.length()))

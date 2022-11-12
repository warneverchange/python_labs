from Point2D import *


class Point3D(Point2D):
    _z: float = 0.0

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        if isinstance(z, float):
            self._z = z

    def __eq__(self, o: object) -> bool:
        if not isinstance(object, Point3D):
            raise TypeError("Argument must have Point3D type")
        return super().__eq__(o) and self.z == object.z

    def __str__(self) -> str:
        return super().__str__()[0:-1:1] + f", {self.z})"

    @property
    def x(self):
        return super().x

    @property
    def y(self):
        return super().y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, float):
            raise TypeError("Value must have float type")
        self._z = value


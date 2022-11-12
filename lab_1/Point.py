class Point:
    _x = 0.0
    _y = 0.0

    def __init__(self, x: float, y: float):
        if isinstance(x, float) and isinstance(y, float):
            self._x = x
            self._y = y

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Point):
            return o._x == self._x and o._y == self._y
        else:
            raise TypeError("The argument must be an instance of the point class or inherit it")

    def __str__(self) -> str:
        return f"({self.x}, {self._y})"

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, _y: float) -> None:
        if not isinstance(_y, float):
            raise TypeError("Ordinate must be float value")
        self._y = _y

    @x.setter
    def x(self, _x: float) -> None:
        if not isinstance(_x, float):
            raise TypeError("Abscissa must be float value")
        self._x = _x




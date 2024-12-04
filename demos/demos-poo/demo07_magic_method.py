class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # méthode appelée par print() ou str() pour obtenir la représentation de l'objet
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    # Méthode utilisée pour avoir une répresentation officielle de l'objet
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    # Surcharge de l'opérateur +
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Surcharger l'opérateur d'égalité ==
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented


if __name__ == "__main__":
    print(["1", 2, 3].__str__())
    print(["1", 2, 3].__repr__())

    point1 = Point(3, 5)
    point2 = Point(3, 5)
    print(point1)
    print(point2)

    point3 = point1 + point2
    print(point3)

    if point1 == point2:
        print("Les points sont aux mêmes positions")
    else:
        print("Les points ne sont pas aux mêmes positions")

class SquareHole:
    def __init__(self, length):
        self.length = length

    def canFit(self, square):
        return square.getSide() <= self.length


class Square:
    def __init__(self, side):
        self.side = side

    def getSide(self):
        return self.side


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


class CircleToSquareAdapter:
    def __init__(self, circle):
        self.circle = circle

    def getSide(self):
        return self.circle.getRadius() * 2

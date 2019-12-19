import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, b):
        return math.sqrt((b.x - self.x)**2 + (b.y - self.y)**2)


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

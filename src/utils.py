import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Return true if two points are eq, false else"""
        return self.x == other.x and self.y == other.y

    def distance(self, b):
        """Return the distance between two points"""
        return math.sqrt(((b.x - self.x)**2) + ((b.y - self.y)**2))


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Rectangle:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        """Return the area of the rectangle"""
        return self.b.distance(self.a) * self.b.distance(self.c)


class Line:

    def __init__(self, point, vect=None, p2=None):
        self.point = point
        if p2 is None:
            self.vect = vect
        elif vect is None:
            if point.x == p2.x:
                self.vect = [0, 1]
            else:
                self.vect = [p2.x - point.x, p2.y - point.y]

    def intersection(self, l):
        """Return the intersection Point between two lines"""
        if self.vect[0] == 0:
            if l.vect[0] == 0:
                return None
            else:
                return Point(self.point.x, l.incline() * self.point.x + l.origin_y())
        if l.vect[0] == 0:
            return Point(l.point.x, self.incline() * l.point.x + self.origin_y())
        if self.incline() == l.incline():
            return None
        x_coord = (l.origin_y() - self.origin_y()) / \
            (self.incline() - l.incline())
        return Point(x_coord, self.incline() * x_coord + self.origin_y())

    def origin_y(self):
        """return the origin of the Line"""
        return self.point.y - self.incline() * self.point.x

    def incline(self):
        """return the slope of the Line"""
        return self.vect[1] / self.vect[0]


def triangleContientPoint(a, b, c, x):
    """Return true if the triangle a,b,c contains x, else false"""
    l1 = ((b.y - c.y) * (x.x - c.x) + (c.x - b.x) * (x.y - c.y)) / \
        ((b.y - c.y) * (a.x - c.x) + (c.x - b.x) * (a.y - c.y))
    l2 = ((c.y - a.y) * (x.x - c.x) + (a.x - c.x) * (x.y - c.y)) / \
        ((b.y - c.y) * (a.x - c.x) + (c.x - b.x) * (a.y - c.y))
    l3 = 1 - l1 - l2
    return 0 < l1 and l1 < 1 and 0 < l2 and l2 < 1 and 0 < l3 and l3 < 1


def crossProduct(p, q, s, t):
    """Return the cross product of p,q,s,t"""
    return (q.x - p.x) * (t.y - s.y) - (q.y - p.y) * (t.x - s.x)


def cosine(a, b):
    """Return the absolute value of the cosine of the angle between two lines"""
    return abs((a.vect[0] * b.vect[0] + a.vect[1] * b.vect[1]) / (math.sqrt(a.vect[0] * a.vect[0] + a.vect[1] * a.vect[1]) * math.sqrt(b.vect[0] * b.vect[0] + b.vect[1] * b.vect[1])))

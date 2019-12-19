from utils import *
import math


def ritter(points):
    if len(points) < 1:
        None
    rest = points[:]  # copie de la liste
    dummy = rest[0]
    p = dummy
    for s in rest:
        if dummy.distance(s) > dummy.distance(p):
            p = s
    q = p
    for s in rest:
        if p.distance(s) > p.distance(q):
            q = s
    cX = 0.5 * (p.x + q.x)
    cY = 0.5 * (p.y + q.y)
    cRadius = 0.5 * p.distance(q)
    rest.remove(p)
    rest.remove(q)
    while not len(rest):
        s = rest.remove(0)
        distanceFromCToS = math.sqrt(
            (s.x - cX) * (s.x - cX) + (s.y - cY) * (s.y - cY))
        if distanceFromCToS <= cRadius:
            continue
        cPrimeRadius = 0.5 * (cRadius + distanceFromCToS)
        alpha = cPrimeRadius / (distanceFromCToS)
        beta = (distanceFromCToS - cPrimeRadius) / (distanceFromCToS)
        cPrimeX = alpha * cX + beta * s.x
        cPrimeY = alpha * cY + beta * s.y
        cRadius = cPrimeRadius
        cX = cPrimeX
        cY = cPrimeY
    return Circle(Point(cX, cY), cRadius)

from utils import *
import sys
import math
import array
import time


def ritter(points):
    """
    Return the smallest bouding Circle given by ritter algorithm
    applied to the points list
    """
    if len(points) < 1:
        return None
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
    while len(rest):
        s = rest.pop()
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


def trie_pixel(points):
    '''Sort the points list'''
    if len(points) < 4:
        return None
    maxX = points[0].x
    for p in points:
        if p.x > maxX:
            maxX = p.x
    maxY = [None for i in range(maxX + 1)]
    minY = [None for i in range(maxX + 1)]
    for p in points:
        if maxY[p.x] is None or p.y > maxY[p.x].y:
            maxY[p.x] = p
        if minY[p.x] is None or p.y < minY[p.x].y:
            minY[p.x] = p
    result = []
    for i in range(maxX + 1):
        if maxY[i] is not None:
            result.append(maxY[i])
    for i in range(maxX, -1, -1):
        if minY[i] is not None and not result[len(result) - 1] == minY[i]:
            result.append(minY[i])
    if result[len(result) - 1] == result[0]:
        del result[len(result) - 1]
    return result


def graham(points):
    """Return the convex hull given by Graham's algorithm"""
    if len(points) < 4:
        return None
    result = trie_pixel(points)
    i = 1
    while i < len(result) + 2:
        p = result[(i-1) % len(result)]
        q = result[i % len(result)]
        r = result[(i+1) % len(result)]
        if crossProduct(p, q, p, r) > 0:
            del result[i % len(result)]
            if i == 2:
                i = 1
            if i > 2:
                i -= 2
        i = i + 1
    return result


def toussaint(points):
    """Return the minimum bouding rectangle given by Toussaint's algorithm"""

    if len(points) < 4:
        return None

    # get convex hull
    enveloppe = graham(points)

    # compute end points
    i_ind = j_ind = k_ind = l_ind = 0
    i_start = j_start = k_start = l_start = 0

    for i in range(1, len(enveloppe)):
        if enveloppe[i].x < enveloppe[i_ind].x:
            i_ind = i
        if enveloppe[i].y < enveloppe[l_ind].y:
            l_ind = i
        if enveloppe[i].x > enveloppe[k_ind].x:
            k_ind = i
        if enveloppe[i].y > enveloppe[j_ind].y:
            j_ind = i

    i_start = i_ind
    j_start = j_ind
    k_start = k_ind
    l_start = l_ind

    # compute lines passing by i,j,k,l
    i_line = Line(enveloppe[i_ind], [0, 1])
    j_line = Line(enveloppe[j_ind], [1, 0])
    k_line = Line(enveloppe[k_ind], [0, -1])
    l_line = Line(enveloppe[l_ind], [-1, 0])

    hullFinished = False
    i_incr = j_incr = k_incr = l_incr = False
    count = 0
    max_cos = 0
    max_cos_ind = 0
    res = Rectangle(i_line.intersection(j_line), j_line.intersection(
        k_line), k_line.intersection(l_line), l_line.intersection(i_line))
    min_area = res.area()
    rect = res

    while not hullFinished:
        # compute corners
        i_cos = cosine(i_line, Line(
            enveloppe[i_ind], None, enveloppe[(i_ind + 1) % len(enveloppe)]))
        j_cos = cosine(j_line, Line(
            enveloppe[j_ind], None, enveloppe[(j_ind + 1) % len(enveloppe)]))
        if i_cos > j_cos:
            max_cos = i_cos
            max_cos_ind = i_ind
        else:
            max_cos = j_cos
            max_cos_ind = j_ind
        k_cos = cosine(k_line, Line(
            enveloppe[k_ind], None, enveloppe[(k_ind + 1) % len(enveloppe)]))
        if k_cos > max_cos:
            max_cos = k_cos
            max_cos_ind = k_ind
        l_cos = cosine(l_line, Line(
            enveloppe[l_ind], None, enveloppe[(l_ind + 1) % len(enveloppe)]))
        if l_cos > max_cos:
            max_cos = l_cos
            max_cos_ind = l_ind

        # rotation
        if max_cos_ind == i_ind:
            i_line = Line(
                enveloppe[i_ind], None, enveloppe[(i_ind + 1) % len(enveloppe)])
            j_line = Line(
                enveloppe[j_ind], [i_line.vect[1], -i_line.vect[0]])
            k_line = Line(
                enveloppe[k_ind], [-i_line.vect[0], -i_line.vect[1]])
            l_line = Line(
                enveloppe[l_ind], [-j_line.vect[0], -j_line.vect[1]])
            i_ind = (i_ind + 1) % len(enveloppe)
            i_line.point = enveloppe[i_ind]
            i_incr = True

        elif max_cos_ind == j_ind:
            j_line = Line(
                enveloppe[j_ind], None, enveloppe[(j_ind + 1) % len(enveloppe)])
            k_line = Line(
                enveloppe[k_ind], [j_line.vect[1], -j_line.vect[0]])
            l_line = Line(
                enveloppe[l_ind], [-j_line.vect[0], -j_line.vect[1]])
            i_line = Line(
                enveloppe[i_ind], [-k_line.vect[0], -k_line.vect[1]])

            j_ind = (j_ind + 1) % len(enveloppe)
            j_line.point = enveloppe[j_ind]
            j_incr = True

        elif max_cos_ind == k_ind:
            k_line = Line(
                enveloppe[k_ind], None, enveloppe[(k_ind + 1) % len(enveloppe)])
            l_line = Line(
                enveloppe[l_ind], [k_line.vect[1], -k_line.vect[0]])
            i_line = Line(
                enveloppe[i_ind], [-k_line.vect[0], -k_line.vect[1]])
            j_line = Line(
                enveloppe[j_ind], [-l_line.vect[0], -l_line.vect[1]])
            k_ind = (k_ind + 1) % len(enveloppe)
            k_line.point = enveloppe[k_ind]
            k_incr = True

        else:
            l_line = Line(
                enveloppe[l_ind], None, enveloppe[(l_ind + 1) % len(enveloppe)])
            i_line = Line(
                enveloppe[i_ind], [l_line.vect[1], -l_line.vect[0]])
            j_line = Line(
                enveloppe[j_ind], [-l_line.vect[0], -l_line.vect[1]])
            k_line = Line(
                enveloppe[k_ind], [-i_line.vect[0], -i_line.vect[1]])
            l_ind = (l_ind + 1) % len(enveloppe)
            l_line.point = enveloppe[l_ind]
            l_incr = True

        # compute rectangle and rectangle area
        rect = Rectangle(i_line.intersection(j_line), j_line.intersection(
            k_line), k_line.intersection(l_line), l_line.intersection(i_line))
        if rect.area() < min_area:
            res = rect
            min_area = rect.area()

        # update finish conditions
        if (i_incr and i_ind == i_start) or (j_incr and j_ind == j_start) or (k_incr and k_ind == k_start) or (l_incr and l_ind == l_start):
            count = count + 1
        hullFinished = (count >= 4)

    return res

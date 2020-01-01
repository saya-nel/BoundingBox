from utils import *
import sys
import math


def ritter(points):
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


def quickHull(points):
    if len(points) < 4:
        return None
    nord = sud = ouest = est = points[0]
    for p in points:
        if p.x < ouest.x:
            ouest = p
        if p.y > sud.y:
            sud = p
        if p.x > est.x:
            est = p
        if p.y < nord.y:
            nord = p
    result = [ouest, sud, est, nord]
    rest = points[:]

    rest = filter(lambda e: not (triangleContientPoint(
        ouest, sud, est, e) or triangleContientPoint(ouest, est, nord, e)), rest)

    i = 0
    while(i < len(result)):
        a = result[i]
        b = result[(i + 1) % len(result)]
        ref = result[(i + 2) % len(result)]
        signeRef = crossProduct(a, b, a, ref)
        maxValue = 0
        maxPoint = a

        for p in points:
            piki = crossProduct(a, b, a, p)
            if signeRef * piki < 0 and abs(piki) > maxValue:
                maxValue = abs(piki)
                maxPoint = p

        if maxValue != 0:
            rest = filter(lambda e: not (triangleContientPoint(
                ouest, sud, est, e) or triangleContientPoint(ouest, est, nord, e)), rest)
            result.insert(i + 1, maxPoint)
            i = i-1
        i = i + 1
    return result


def toussaint(points):

    if len(points) < 4:
        return None

    # on récupère l'enveloppe convexe
    enveloppe = quickHull(points)

    #   // Première étape : On cherche les quatre points extremes
    index_i = index_j = index_k = index_l = 0
    index_i0 = index_j0 = index_k0 = index_l0 = 0

    for i in range(1, len(enveloppe)):
        if enveloppe[i].x < enveloppe[index_i].x:
            index_i = i
        if enveloppe[i].y < enveloppe[index_l].y:
            index_l = i
        if enveloppe[i].x > enveloppe[index_k].x:
            index_k = i
        if enveloppe[i].y > enveloppe[index_j].y:
            index_j = i
    if index_i == index_j or index_i == index_k or index_i == index_l or index_j == index_k or index_j == index_l or index_k == index_l:
        return None
    index_i0 = index_i
    index_j0 = index_j
    index_k0 = index_k
    index_l0 = index_l

#   // Deuxième étape : On initialise les lignes de support
    support_i = Line(enveloppe[index_i], [0, 1])
    support_j = Line(enveloppe[index_j], [1, 0])
    support_k = Line(enveloppe[index_k], [0, -1])
    support_l = Line(enveloppe[index_l], [-1, 0])

    hullScanned = False  # cond arret
    iStepped = jStepped = kStepped = lStepped = False  # cond arret
    count = 0
    # angle min
    cos_theta_max = 0
    index_cos_max = 0
    res = Rectangle(support_i.intersection(support_j), support_j.intersection(
        support_k), support_k.intersection(support_l), support_l.intersection(support_i))
    areaMin = res.area()
    rect = res  # rect actu
#   // Tant que l'on n'a pas fini de parcourir l'enveloppe convexe.
    while not hullScanned:
        # calcul des angles
        cos_theta_i = cosine(support_i, Line(
            enveloppe[index_i], None, enveloppe[(index_i + 1) % len(enveloppe)]))
        cos_theta_j = cosine(support_j, Line(
            enveloppe[index_j], None, enveloppe[(index_j + 1) % len(enveloppe)]))
        if cos_theta_i > cos_theta_j:
            cos_theta_max = cos_theta_i
            index_cos_max = index_i
        else:
            cos_theta_max = cos_theta_j
            index_cos_max = index_j

        cos_theta_k = cosine(support_k, Line(
            enveloppe[index_k], None, enveloppe[(index_k + 1) % len(enveloppe)]))
        if cos_theta_k > cos_theta_max:
            cos_theta_max = cos_theta_k
            index_cos_max = index_k

        cos_theta_l = cosine(support_l, Line(
            enveloppe[index_l], None, enveloppe[(index_l + 1) % len(enveloppe)]))
        if cos_theta_l > cos_theta_max:
            cos_theta_max = cos_theta_l
            index_cos_max = index_l

#     /*
#      * Quatrième étape : On fait avancer le point correspondant à l'angle
#      * minimum. Sa ligne support est alors confondue avec le prochain coté de
#      * l'enveloppe convexe, et on détermine les trois autres lignes de support
#      * en fonction de celle-ci (orthogonale / inverse)
#      */
        if index_cos_max == index_i:
            support_i = Line(
                enveloppe[index_i], None, enveloppe[(index_i + 1) % len(enveloppe)])
            support_j = Line(
                enveloppe[index_j], [support_i.vect[1], -support_i.vect[0]])
            support_k = Line(
                enveloppe[index_k], [-support_i.vect[0], -support_i.vect[1]])
            support_l = Line(
                enveloppe[index_l], [-support_j.vect[0], -support_j.vect[1]])

            index_i = (index_i + 1) % len(enveloppe)
            support_i.point = enveloppe[index_i]
            # // Le point i a bougé(condition d'arrêt)
            iStepped = True
        elif index_cos_max == index_j:
            support_j = Line(
                enveloppe[index_j], None, enveloppe[(index_j + 1) % len(enveloppe)])
            support_k = Line(
                enveloppe[index_k], [support_j.vect[1], -support_j.vect[0]])
            support_l = Line(
                enveloppe[index_l], [-support_j.vect[0], -support_j.vect[1]])
            support_i = Line(
                enveloppe[index_i], [-support_k.vect[0], -support_k.vect[1]])

            index_j = (index_j + 1) % len(enveloppe)
            support_j.point = enveloppe[index_j]
        # // Le point j a bougé (condition d'arrêt)
            jStepped = True

        elif index_cos_max == index_k:
            support_k = Line(
                enveloppe[index_k], None, enveloppe[(index_k + 1) % len(enveloppe)])
            support_l = Line(
                enveloppe[index_l], [support_k.vect[1], -support_k.vect[0]])
            support_i = Line(
                enveloppe[index_i], [-support_k.vect[0], -support_k.vect[1]])
            support_j = Line(
                enveloppe[index_j], [-support_l.vect[0], -support_l.vect[1]])

            index_k = (index_k + 1) % len(enveloppe)
            support_k.point = enveloppe[index_k]
            # // Le piont k a bougé (condition d'arrêt)
            kStepped = True

        else:
            support_l = Line(
                enveloppe[index_l], None, enveloppe[(index_l + 1) % len(enveloppe)])
            support_i = Line(
                enveloppe[index_i], [support_l.vect[1], -support_l.vect[0]])
            support_j = Line(
                enveloppe[index_j], [-support_l.vect[0], -support_l.vect[1]])
            support_k = Line(
                enveloppe[index_k], [-support_i.vect[0], -support_i.vect[1]])
            index_l = (index_l + 1) % len(enveloppe)
            support_l.point = enveloppe[index_l]
            # // Le point l a bougé (condition d'arrêt)
            lStepped = True

#     // Cinquième étape : On calcule l'aire du rectangle.

        rect = Rectangle(support_i.intersection(support_j), support_j.intersection(
            support_k), support_k.intersection(support_l), support_l.intersection(support_i))
        # // Mise à jour du rectangle minimum
        if rect.area() < areaMin:
            res = rect
            areaMin = rect.area()
#     // Si l'un des points a bougé et qu'il est revenu à son point de
#     // départ
        if (iStepped and index_i == index_i0) or (jStepped and index_j == index_j0) or (kStepped and index_k == index_k0) or (lStepped and index_l == index_l0):
            count = count + 1
        hullScanned = (count >= 4)
    return res

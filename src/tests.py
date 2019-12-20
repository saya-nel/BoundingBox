import os
from utils import *


def get_points_from_file(fic):
    f = open(fic, 'r')
    res = []
    for line in f:
        coords = line.split()
        res.append(Point(int(coords[0]), int(coords[1])))
    return res


def gen_lists():
    tests_files = ["samples/" + f for f in os.listdir("samples")]
    for fic in tests_files:
        yield get_points_from_file(fic)

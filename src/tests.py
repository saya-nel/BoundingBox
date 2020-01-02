import os
import time
import random
from utils import *
from algorithms import *


def get_points_from_file(fic):
    """Return all the Point from a file path"""
    f = open(fic, 'r')
    res = []
    for line in f:
        coords = line.split()
        res.append(Point(int(coords[0]), int(coords[1])))
    f.close()
    return res


def gen_lists():
    """Return the generator that allow to get all points from a testing file"""
    tests_files = ["samples/" +
                   f for f in os.listdir("samples") if f != "test-1.points"]
    for fic in tests_files:
        yield get_points_from_file(fic), fic


def get_all_points():
    """Return all the Point of testing files concatenated in one list"""
    g = gen_lists()
    res = []
    for n, _ in g:
        res = res + n
    return res


def execution_time(f, arg):
    """Return the execution time of the function f apply with arg"""
    start_time = time.time()
    f(arg)
    return time.time() - start_time


def algorithms_time(gap):
    """Return the executions times for Toussaint's and Ritter's algorithms"""
    touss = []
    rit = []
    print("load points from test base")
    points = get_all_points()
    for i in range(256, len(points), gap):
        print("testing for size " + str(i))
        touss.append(execution_time(toussaint, points[:i]))
        rit.append(execution_time(ritter, points[:i]))
    return touss, rit


def quality(points):
    """Return the quality of toussaint's and ritter's containers"""
    p_area = polygon_area(graham(points))
    touss_area = toussaint(points).area()
    ritt_area = ritter(points).area()
    touss_quality = (touss_area / p_area) - 1
    ritt_quality = (ritt_area / p_area) - 1
    return touss_quality, ritt_quality


def algorithms_quality():
    """Return algorithms qualities in all test files"""
    gen = gen_lists()
    touss_qualities = []
    ritt_qualities = []
    i = 0
    for points, f in gen:
        i = i+1
        print("testing quality for file : ", f)
        touss_quality, ritt_quality = quality(points)
        touss_qualities.append(touss_quality)
        ritt_qualities.append(ritt_quality)
    return touss_qualities, ritt_qualities

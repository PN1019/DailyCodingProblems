#This problem was asked by LinkedIn.[Hard]

#Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

#Solution using itemgetter():
# operator.itemgetter(n) constructs a callable that assumes an iterable object (e.g. list, tuple, set) as input, and fetches the n-th element out of it.
# The key= parameter of sort requires a key function (to be applied to be objects to be sorted) rather than a single key value and
# that is just what operator.itemgetter(1) will give you: A function that grabs the first item from a list-like object.

from operator import itemgetter
def kNearestPoints(points, central_point, k):
# input: list of points (x, y), a central point (x_C, y_c) & int k
# output: list of k nearest points from central point
    # trival cases
    if k <= 0:
        return []
    if k >= len(points):
        return points
    # else
    x_c = central_point[0]  # x-coordinate of central point
    y_c = central_point[1]  # y-coordinate of central point
    distance_list = []      # list of [point (x,y), distance to central point] initialized
    kList = []              # list of k nearest points initialized
    # compute distance from each points to central points, then push entry into distance_list
    for point in points:
        x = point[0]
        y = point[1]
        d = (x - x_c)**2 + (y - y_c)**2     # distance ^ 2
        distance_list.append([point, d])
    distance_list = sorted(distance_list, key=itemgetter(1))    # sort distance_list ascendingly by distance
    # add k nearest points into kList
    for i in range(k):
        chosenPoint = distance_list[i][0]
        kList.append(chosenPoint)
    return kList
# Tests
assert kNearestPoints(
    [(0, 0), (5, 4), (3, 1)],(1, 2), 2) == [(0, 0), (3, 1)]

#Solution using sqrt() :
# here targets = list of points(x,y) , source = central points(x_C, y_c)
import math

# compute distance from each points to central points using sqrt()
def compute_distance(source, target):
    return math.sqrt(
        (source[0] - target[0]) ** 2 +
        (source[1] - target[1]) ** 2
    )


def kNearestPoints(targets, source, k):
    if k >= len(targets):
        return targets
# sort targets by calculate_distance and return nearest_points
    nearest_points = \
        sorted(targets, key=lambda x: compute_distance(source, x))[:k]

    return nearest_points



# Tests
assert compute_distance((0, 0), (3, 4)) == 5
assert kNearestPoints(
    [(0, 0), (5, 4), (3, 1)],(1, 2), 2) == [(0, 0), (3, 1)]

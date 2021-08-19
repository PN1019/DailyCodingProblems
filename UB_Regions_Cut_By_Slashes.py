#This problem was asked by Uber.(Medium)

#You are given a 2-d matrix where each cell consists of either /, \, or an empty space. Write an algorithm that determines into how many regions the slashes divide the space.

#For example, suppose the input for a three-by-six grid is the following:

#\    /
 #\  /
  #\/
#Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.

# Solution:

from typing import Set
from random import sample


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash("{}-{}".format(self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "[x={}, y={}]".format(self.x, self.y)


def explore_region(start: Coord, empty_spaces: Set, nrows: int, ncols: int):
    if start not in empty_spaces:
        return

    empty_spaces.remove(start)
    if start.x > 0:
        explore_region(Coord(start.x - 1, start.y), empty_spaces, nrows, ncols)
    if start.x < nrows - 1:
        explore_region(Coord(start.x + 1, start.y), empty_spaces, nrows, ncols)
    if start.y > 0:
        explore_region(Coord(start.x, start.y - 1), empty_spaces, nrows, ncols)
    if start.y < ncols - 1:
        explore_region(Coord(start.x, start.y + 1), empty_spaces, nrows, ncols)


def get_region_count(text: str):
# splitlines() is a built-in method that returns a list of the lines in the string, breaking at line boundaries.
# to build 2d matrix
    matrix = text.splitlines()
    nrows, ncols = len(matrix), len(matrix[0])
    for i in range(nrows):
        matrix[i] = [x for x in matrix[i]]

    empty_spaces = set()
    for row in range(nrows):
        for col in range(ncols):
            if matrix[row][col] == " ":
                empty_spaces.add(Coord(row, col))
#to find zero regions
    regions = 0
    while empty_spaces:
    # sample() is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for random sampling without replacement
        start = sample(empty_spaces, 1)[0]
        explore_region(start, empty_spaces, nrows, ncols)
        regions += 1

    return regions


# Tests
matrix = \
    "\\    /\n" + \
    " \\  / \n" + \
    "  \\/  "
assert get_region_count(matrix) == 3

matrix = \
    "     /\n" + \
    " \\  / \n" + \
    "  \\/  "
assert get_region_count(matrix) == 2

matrix = \
    "     /\n" + \
    " \\  / \n" + \
    "  \\   "
assert get_region_count(matrix) == 1

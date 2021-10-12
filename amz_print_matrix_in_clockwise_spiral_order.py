"""
This problem was asked by Amazon.[EASY]
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""
#Solution using zip functionality:
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
        
        result = []
        
        while matrix:
            result += matrix.pop(0)
            
            matrix = (list(zip(*matrix)))[::-1]
        
        return result

matrix=[[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]
assert spiralOrder(matrix) == [
    1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
#Solution using python one-liner:
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
# Solution using Simulation approach:O(M*N)
def spiralOrder(matrix):
        n, m ,VISITED = len(matrix[0]), len(matrix),"*"
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m*n):
            if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == VISITED:# If out of bound or already visited
                dx, dy = -dy, dx # to rotate orientation
                
            ans.append(matrix[y][x])
            matrix[y][x] = VISITED # Mark as VISITED 
            x, y = x + dx, y + dy
        
        return ans
matrix=[[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]
assert spiralOrder(matrix) == [
    1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

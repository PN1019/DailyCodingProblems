#This problem was asked by LinkedIn.[Hard]

#Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
#Solution By Sort:
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda P:P[0]**2+P[1]**2)
        return points[:K]
sol=Solution()
points = [[3, 3], [5, -1], [-2, 4]]
#points=[[0, 0], [5, 4], [3, 1]]
K = 2
 
print(sol.kClosest(points, K))        
#Time complexity: O(NlogN)
#Sort the list according to the distance to origin. 
#Apparently, we did more than the question asked. We sorted all the distance, the question only ask for top k.
#To improve time complexity, we need to think about how to get we ask without extra effort. This is where heap data structure comes in.

# Solution by Max Heap Approach:
import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist, point))
            if len(heap) > K:
                heapq.heappop(heap)
    
        return [tuple[1] for tuple in heap]
sol=Solution()
#points2 = [[3, 3], [5, -1], [-2, 4]]
points1=[[0, 0], [5, 4], [3, 1]]
K = 2
 
print(sol.kClosest(points1, K))        
#result1=[(0, 0), (3, 1)]
#result2=[[-2, 4], [3, 3]]    
    
# Time compiexity: O(NlogK)
# heapq is a binary heap, with O(log n) push and O(log n) pop. n is the size of the minimum heap. In this case, n = K.
# So the time complexity is Nlog(K)
#Solution by quick sort:
class Solution:
    def kClosest(self, points, K):
        self.sort(points, 0, len(points)-1, K)
        return points[:K]
    
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points, l, p-1, K)
            
    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]                
        return a
sol=Solution()
points = [[3, 3], [5, -1], [-2, 4]]
#points=[[0, 0], [5, 4], [3, 1]]
K = 2
 
print(sol.kClosest(points, K))
#Time Complexity: Quick Sort - O(N) on average



#This problem was asked by LinkedIn.[Hard]

#Given a list of points and an integer k, find the nearest k points from the origin.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)] and k = 2, return [(0, 0), (3, 1)].
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
print(f"The nearest {K} neighbors {points} from the origin are{sol.kClosest(points, K)}")  
#result1=[[-2, 4], [3, 3]]
#result2=[(0, 0), (3, 1)]
    
       
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
print(f"The nearest {K} neighbors {points} from the origin are{sol.kClosest(points, K)}")  
#result1=[[-2, 4], [3, 3]]
#result2=[(0, 0), (3, 1)]
       
    
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
print(f"The nearest {K} neighbors {points} from the origin are{sol.kClosest(points, K)}")  
#result1=[[-2, 4], [3, 3]]
#result2=[(0, 0), (3, 1)]
#Time Complexity: Quick Sort - O(N) on average
     
#Solution by Kd-tree Approach for large no. of queries:
# What if I have 10 million points now and I have to perform the search 10000 times? How would you optimize it?
from scipy import spatial
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=K, p=2) 
        return [points[i] for i in idx] if K > 1 else [points[idx]]
sol=Solution()
#points = [[3, 3], [5, -1], [-2, 4]]
points=[[1, 3], [5, 4], [3, 1]]
K = 2
 
print(f"The nearest {K} neighbors {points} from the origin are{sol.kClosest(points, K)}")        
#result1=[[-2, 4], [3, 3]]
#result2=[(1, 3), (3, 1)]


# kd-tree has the following comeplexity:

# Build the tree - O(NlogN), building the tree requires presorting the points and find the medians (but we only need to do this once).
# Search, Insert, Delete - O(logN), similar to how a normal binary tree works (with a tree balancing mechanism)
# Now, as we can see, it greatly reduces the time complexity for each nearest neighbor query to O(logN), and if we need to find the K closest points, the total complexity will be O(KlogN).
# This is great if we have a lot of points and we are only interested in a few neighbors.




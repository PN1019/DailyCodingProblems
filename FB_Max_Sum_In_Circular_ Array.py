
# This problem was asked by Facebook.


# Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

# Solution:
#Bascially Algo. in Steps here:
#1. Find maximum subarray sum using kadane's algorithm (max) 
#2. Find minimum subarray sum using kadane's algorithm (min)
#3. Find total sum of the array (sum)
#4. Now, if sum == min return max
#5. Otherwise, return maximum ( max, sum - min )


class Solution:
    
    def maxSubarraySumCircular(self, A):
        if len(A) == 0:#in case of empty sub-array 
            return 0
        maxTotal,maxSoFar,minSoFar,minTotal,sum = A[0], A[0], A[0], A[0],A[0]
        for i in range(1, len(A)):
            maxSoFar = max(A[i], maxSoFar + A[i])
            maxTotal = max(maxTotal, maxSoFar)            
            
            minSoFar = min(A[i], minSoFar + A[i])            
            minTotal = min(minTotal, minSoFar)            
            sum += A[i]
        if(sum == minTotal):
            return maxTotal
        
        return max(sum - minTotal, maxTotal);
KDEAlgo=Solution()
 
#A = [8, -1, 3, 4]#input case 
#A = [-8, -3, -6, -2, -5, -4]#input case of all negatives
#A=[-4, 5, 1, 0]
A=[] #input case of empty
 
print("The maximum circular subarray sum is",KDEAlgo.maxSubarraySumCircular(A))

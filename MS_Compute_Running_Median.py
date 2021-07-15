This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

## Solution by using Bisect:
from bisect import insort

class MedianFinder:

    def __init__(self):
        self.nums = []      
        
    def addNum(self, num: int) -> None:
        insort(self.nums,num)

    def findMedian(self) -> float:
        length = len(self.nums)
        if length == 0: return None
        if length == 1: return self.nums[0]
        mid = length//2
        if length%2 == 0:
            return ((self.nums[mid]+self.nums[mid-1])/2)##even
        return self.nums[mid]#odd
obj = MedianFinder()
obj.addNum(2)
par0= obj.findMedian()
obj.addNum(1)
par1= obj.findMedian()
obj.addNum(5)
par2=obj.findMedian()
obj.addNum(7)
par3=obj.findMedian()
obj.addNum(2)
par4=obj.findMedian()
obj.addNum(0)
par5=obj.findMedian()
obj.addNum(5)
par5 = obj.findMedian()
print(par0,par1,par2,par3,par4,par5,par5,sep="\n")
            
        
        

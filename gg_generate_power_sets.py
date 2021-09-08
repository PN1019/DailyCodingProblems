#This problem was asked by Google.

#The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

#For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

#You may also use a list or array to represent a set.
#Solution using Iterative Approach :
def powersets(setOfNumbers):
    totalNumberSets = 2 ** (len(setOfNumbers))
    binarySize = len('{0:b}'.format(totalNumberSets - 1))
    binaryMask = '{0:0' + str(binarySize) + 'b}'
    powers = []
    for index in range(totalNumberSets):
        combination = binaryMask.format(index)
        subSet = []
        for i in range(len(combination)):
            if combination[i] == '1':
                subSet += [setOfNumbers[i]]
        powers.append(subSet)
    return powers

if __name__ == "__main__":
    print(powersets([1, 2, 3]))

#Solution using itertools.combinations:
import itertools
from functools import reduce
import operator 
class Solution():
    def powersets(self,l):
        iters = map((lambda i:itertools.combinations(l, i)),range(len(l)+1))
        iters = map(list,iters)
        return reduce(operator.__add__, iters ,[])
        
sol=Solution()
nums = [1,2,3]
fx_sets=sol.powersets(nums)
print(fx_sets)
#Solution using List Comprehension Method :
def powersets(fullset):
  listrep = list(fullset)
  n = len(listrep)
  return [[listrep[k] for k in range(n) if i&1<<k] for i in range(2**n)]
string=[1,2,3]
print(powersets(string))
#Solution by Bit Mapping:The bit serial from 0 to 2^n - 1 can be mapped to element selction for subset generation.

#Take nums = [1,2,3] for example.

#size of input = 3.
#Thus, we go through bit serial from 0 to 2^3 -1 = ( 1 << 3 ) - 1 = 7, then getting corresponding subset on the fly.
#0 = 0b 000 = empty set = [ ]
#1 = 0b 001 = select first element = [ 1 ]
#2 = 0b 010 = select second element = [ 2 ]
#3 = 0b 011 = select first and second elements = [ 1, 2 ]
#4 = 0b 100 = select third element = [ 3 ]
#5 = 0b 101 = select first and third elements = [ 1, 3 ]
#6 = 0b 110 = select second and third elements = [ 2, 3 ]
#7 = 0b 111 = select all elements = [ 1, 2 , 3 ]

class Solution:
    
    def powersets(self, nums):
    
        size = len(nums)
        upper_bound = 1 << size
		
        return [ [ nums[i]  for i in range(size) if bits_sn & (1 << i) != 0 ] for bits_sn in range(upper_bound) ]
sol=Solution()
nums = [1,2,3]
fx_sets=sol.powersets(nums)
print(fx_sets)

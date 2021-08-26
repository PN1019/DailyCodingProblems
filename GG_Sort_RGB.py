#This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
# You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

#Solution 
# Dutch National Flag Problem
# count Sort Concept 
def sortRGB(self,nums):
    cR = cG = cB = 0
    for num in nums:
        if num == 0:
            cR += 1
        elif num == 1:
            cG += 1
        else:
            cB += 1
    nums[:cR] = [0] * cR
    nums[cR:cR+cG] = [1] * cG
    nums[cR+cG:] = [2] * cB
    return nums

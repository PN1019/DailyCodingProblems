#This problem was asked by Amazon.

#Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

#For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

#Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

#Do this in O(N) time.
#Solution:kadane's algo
def max_subarray(arr):
    if not arr or max(arr) < 0:
        return 0

    current_max_sum = arr[0]
    overall_max_sum = arr[0]

    for num in arr[1:]:
        current_max_sum = max(num, current_max_sum + num)
        overall_max_sum = max(overall_max_sum, current_max_sum)

    return overall_max_sum


assert max_subarray([34, -50, 42, 14, -5, 86]) == 137
assert max_subarray([-5, -1, -8, -9]) == 0


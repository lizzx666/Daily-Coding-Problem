# Given an array of numbers, find the maximum sum of any contiguous subarray of the array. 
# For example, given the array [-34, -50, 42, 14, -5, 86], the maximum sum would be 137, 
# since we would take elements 42, 14, -5, and 86. Given the array [-5, -1, -8, -9], 
# the maximum sum would be 0, since we would choose not to take any elements.

# Do this in O(n) time.

# Follow-up: What if the elements can wrap around? For example, given [8, -1, 3, 4], return 15, 
# as we choose the numbers 3,4 and 8 where 8 is obtained from wrapping around.














def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for i in arr:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far



# Follow-up
def maximum_circular_subarray(arr):
    
    def max_subarray_sum(arr):
        max_ending_here = max_so_far = 0
        for i in arr:
            max_ending_here = max(i, max_ending_here + i)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def min_subarray_sum(arr):
        min_ending_here = min_so_far = 0
        for i in arr:
            min_ending_here = min(i, min_ending_here + i)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far

    max_subarray_wraparound = sum(arr) - min_subarray_sum(arr)
    return max(max_subarray_sum(arr),max_subarray_wraparound)

# Given an array of integers, return a new array where each element in the new array
# is the number of smaller elements to the right of that element in the original input array.

# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There is no smaller element to the right of 1











#method 1: naive solution
def smaller_counts_naive(lst):
    result = []
    for i,num in enumerate(lst):
        count = sum(val < num for val in lst[i+1:])
        result.append(count)
        
    return result   


#method 2:
def smaller_counts(lst):
    result = []
    seen = []
    
    for num in reversed(lst):
        i = bisect.bisect_left(seen,num)
        result.append(i)
        bisect.insort(seen,num)
        
    return list(reversed(result)) 


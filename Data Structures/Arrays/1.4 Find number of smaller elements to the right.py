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
#bisect: Maintains a list in sorted order without having to call sort each time an item is added to the list
#bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, 
#where the number passed in argument can be placed so as to maintain the resultant list in sorted order. 
#If the element is already present in the list, the left most position where element has to be inserted is returned.

#bisect_right = bisect : If the element is already present in the list, the left most position where element has to be inserted is returned.

#insort(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, 
#if the element is already present in the list, the element is inserted at the rightmost possible position. 

#insort =  insort_right
#insort left:if the element is already present in the list, the element is inserted at the leftmost possible position. 
def smaller_counts(lst):
    result = []
    seen = []
    
    for num in reversed(lst):
        i = bisect.bisect_left(seen,num)
        result.append(i)
        bisect.insort(seen,num)
        
    return list(reversed(result)) 


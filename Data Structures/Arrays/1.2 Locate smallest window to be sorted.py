#Given an array of integers that are out of order, determine the bounds of the smallest 
#window that must be sorted in order for the entire array to be sorted.
#For example, given [3,7,5,6,9], you should return (1,3)














#method 1:
def window(array):
    left, right = None, None
    s = sorted(array)
    
    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i
            
    return (left,right)

window([2,3,4,7,6,5,9,8])  

#method 2:

def window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = - float("inf"), float("inf")
    
    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
            
    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i
            
    return(left, right)

window([2,3,4,7,6,5,9])  



##extra: if require to return (start, window length)
#method 1:
def window(array):
    length = 0
    k = 0
    l = len(array) - 1
    while k>=0 and array[k]<=array[k+1]:
        k+=1
        if k == len(array)-2:
            return (1,0)
    while array[k]<array[l]:
        l-=1
    return (k,l-k+1)

window([2,3,4,7,5,2,8,6])  

#method 2:
def window(array):
    length = 0
    k = 0
    for i in range(0,len(array)-1):
        if (array[i] > array[i+1]):
            k = i+1
            length = 1
            while array[k] < array[i]:
                length += 1
                k+=1
                if k == len(array)-2:
                    return (i,len(array)-i)
    return (i,length)

window([2,3,4])  

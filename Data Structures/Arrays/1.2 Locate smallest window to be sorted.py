#Given an array of integers that are out of order, determine the bounds of the smallest 
#window that must be sorted in order for the entire array to be sorted.
#For example, given [3,7,5,6,9], you should return (1,3)


def window(array):
    length = 0
    k = 0
    l = len(array) - 1
    while k>=0 and array[k]<=array[k+1]:
        k+=1
    if k == len(array)-2:
        return 0
    while array[k]<array[l]:
        l-=1
    return (k,l-k+1)

window([2,3,4,7,5,2,8,6])  

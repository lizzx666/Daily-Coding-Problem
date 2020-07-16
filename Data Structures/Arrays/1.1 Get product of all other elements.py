
#method 1:
def products(nums):
    new_array = []
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        result = 1
        for i in range(len(new_nums)):
            result = result * new_nums[i]
        new_array.append(result)    
        
    return new_array
 
    
nums = [1,2,3,4,5]        

print(products(nums)) 

#method 2:
def products(nums):
    prefix_products = []
    for num in nums:
        if prefix_products:
          prefix_products.append(prefix_products[-1] * num)
        else:
          prefix_products.append(num)
     
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = suffix_products[::-1]
        
        
    result = []
    for i in range(0,len(nums)):
        if i == 0:
            result.append(suffix_products[i+1])  
        elif i == (len(nums) - 1):
                result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
        
    return result

nums = [1,2,3,4,5]        

print(products(nums)) 
        
        
    


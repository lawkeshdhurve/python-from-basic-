def thirdMax( nums):
    
        
    nums = set(nums)
        
        
    if len(nums) < 3:
        return max(nums)
        
       
    nums.remove(max(nums))  
    nums.remove(max(nums))  
        
    return max(nums)

print(thirdMax([1,2,3,4,5,6]))
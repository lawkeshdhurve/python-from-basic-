def missingNumber(nums):
    c = max(nums)
        
        
    for i in range(c + 1):
        if i not in nums:
            return i
        
       
    return c + 1
    
    
num = [3,0,1]
print(missingNumber(num))
def findDisappearedNumbers(nums):
    s = set(nums)   
    e = []
        
       
    for i in range(1, len(nums) + 1):
        if i not in s:
            e.append(i)  
        
    return e

print(findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))


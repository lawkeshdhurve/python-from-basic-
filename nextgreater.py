def nextGreaterElement(nums1, nums2):
        
       
    next_greater = {}
    stack = []
        
        
    for num in nums2:
           
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
            
        stack.append(num)
        
        
    while stack:
        next_greater[stack.pop()] = -1
        
       
    return [next_greater[num] for num in nums1]

print(nextGreaterElement([2,4],[1,2,3,4]))
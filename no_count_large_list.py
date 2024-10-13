def majorityElement(nums):
        r = list(set(nums)) 
        c = []  

        
        for item in r:  
            c.append(nums.count(item))

        
        l = max(c)

        
        return r[c.index(l)]
    
n = [2,3,4,2,3,2,3]
print(majorityElement(n))
 


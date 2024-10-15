




def isPowerOfTwo( n):
    d = 2
        
    if n ==0:
        if n==d**n:
            return True
        else:
            return False
    elif n == 1:
        return True
    t = n
    count =0
    while t > 1:
        if t % d != 0:
            return False
                
        else:
            t //= 2
            count += 1
            
    if n == d**count:
        return True
    
            
        
 
isPowerOfTwo(4)
    
    
    
    
    
    
    



    
    

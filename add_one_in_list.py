def plusOne(digits):
        s = ""
        d = 0
        r = []
        for d in digits:
            s += str(d)
            
        d = int(s) + 1
        d = str(d)
        
        for t in d:
            t = int(t)
            r.append(t)
            
            
            
        return  r
    
    
digits = [1,2,3]
print(plusOne(digits))

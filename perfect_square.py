def isPerfectSquare(num):
    if num == 1:
        return True  
        
    for i in range(1, int(num**0.5) + 1):  
        if i * i == num:
            return True
            
    return False


print(isPerfectSquare(16))
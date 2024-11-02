
def isSubsequence(self, s, t):
        
    t_iter = iter(t)
        
    for char in s:
           
        if char not in t_iter:
            return False
    return True


s = "abc"
t = "ahbgdc"

print(isSubsequence( s , t))
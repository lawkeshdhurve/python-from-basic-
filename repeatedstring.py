def repeatedSubstringPattern( s):
        
    for i in range(1, len(s) // 2 + 1):
            
        if len(s) % i == 0:
                
            c = s[:i]
                
            if c * (len(s) // i) == s:
                return True
    return False

print(repeatedSubstringPattern("abcabcabc"))
print(repeatedSubstringPattern("abcd"))
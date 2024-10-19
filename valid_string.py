def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
  
    if len(s) != len(t):
        return False

    
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

   
    return all(value == 0 for value in count.values())

print(isAnagram("listen", "silent"))  # Output: True
print(isAnagram("rat", "car"))        
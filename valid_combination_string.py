def validsymbol(text):
    stack = []
    valid_pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in text:
        if char in valid_pairs:  
            stack.append(char)
        elif char in valid_pairs.values():  
            if not stack or valid_pairs[stack.pop()] != char:  
                return "Invalid"
    
    if stack:  
        return "Invalid"
    
    return "Valid"

def validatestring(text):
    if text.isdigit():
        return "Invalid symbol: it contains digits"
    elif text.isalpha():
        return "Invalid symbol: it contains alphabet"
    else:
        return validsymbol(text)

text = input("Enter your string: ")
print(validatestring(text))

def validsymbol(text):
    valid_string = { '{','}','<','>','[',']','(',')'}
    for char in text:
        if char not in valid_string:
            return "Invalid"
            
        return "valid"
    
def validatestring(text):
    if(text.isdigit()):
        return "Invalid symbol: it contain digit"
    elif(text.isalpha()):
        return "Invalid Symbol : it contain alphabetical"
    else:
        return validsymbol(text)

	    
	    
text = str(input("enter your string : "))
print(validatestring(text))
	    
	    

	


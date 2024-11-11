def findWords( words):
       
        
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
        
        
    result = []
        
        
    for word in words:
            
        lower_word_set = set(word.lower())
            
            
        if lower_word_set <= row1 or lower_word_set <= row2 or lower_word_set <= row3:
            result.append(word)
                
    return result


print(findWords(w = ["Hello","Alaska","Dad","Peace"]))

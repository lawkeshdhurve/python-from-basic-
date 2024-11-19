def detectCapitalUse( word):
    return word.isupper() or word.islower() or word.istitle()



print(detectCapitalUse("Lawkesh"))
print(detectCapitalUse("LAWKESH"))
print(detectCapitalUse("lawkesh"))
    
    
    
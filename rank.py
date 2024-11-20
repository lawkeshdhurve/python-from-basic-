def findRelativeRanks( score):
        
        
    sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
      
    ranks = [""] * len(score)
    for i, (index, _) in enumerate(sorted_scores):
        if i == 0:
            ranks[index] = "Gold Medal"
        elif i == 1:
            ranks[index] = "Silver Medal"
        elif i == 2:
            ranks[index] = "Bronze Medal"
        else:
            ranks[index] = str(i + 1)
        
    return ranks


print(findRelativeRanks([5,3,2,1,4]))

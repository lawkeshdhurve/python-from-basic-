def fun(n,b):
    for char in n :
        if char in b:
            print("True")
        else:
            print("False")
        
    
    
    
    
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]    
n = "ABCDE"
fun(n , board)
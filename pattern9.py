
def fun(n):
	a = ""
	for i in range(n):
		a += '1'
		b = int(a)
	for j in range(n):
	    print(b*n)
	    
	    n -= 1
	    b = int(b / 10)
	    
	    

	    
		
n= int(input("enter : "))
fun(n)

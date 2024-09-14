def fun(n):
    a = ""
    i=1
    for i in range(1,n+1):
        a += '1'
        b = int(a)
        print(b * i)
        
n= int(input("enter : "))
fun(n)


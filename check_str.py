a = input()
b = input()
e = int(input())
d = len(b)
f = False
for i in range(d):
    if b[i] == a[e+i]:
        f = True
    else:
        f = False
        break
        
    
print(f)

def example(s , k):
    c = s[:k]
    a = list(reversed(c))
    return "".join(a) + s[k: ]








s = input()
k = int(input())
print(example(s,k))
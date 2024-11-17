def convertToBase7( num):
    if num == 0:
        return "0"
    negative = num < 0
    num = abs(num)
    base7 = []
    while num:
        base7.append(str(num % 7))
        num //= 7
    if negative:
        base7.append('-')
    return ''.join(reversed(base7))

print(convertToBase7(100))
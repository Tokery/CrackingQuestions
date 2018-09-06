import math

def isPowerOfTwo(n):
    return (n != 0) and (n & (n-1)) == 0

def recMult(a,b):
    if a == 0 or b == 0:
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    elif isPowerOfTwo(a):
        return b << int(math.log(a, 2))
    elif isPowerOfTwo(b):
        return a << int(math.log(b, 2))
    elif b < a:
        return recAdd(a, b)
    else:
        return recAdd(b, a)

def recAdd(y, z):
    if z == 0:
        return 0
    return y + recAdd(y, z-1)

print recMult(4, 0)
print recMult(4, 1)
print recMult(4, 3)
print recMult(5, 3)

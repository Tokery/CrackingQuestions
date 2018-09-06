def checkForMagicIndex(A):
    return magicIndex(A, 0)

def magicIndex(A, adj):
    n = len(A)
    if (n==1):
        return A[n/2]-adj == n/2
    elif A[n/2]-adj == n/2:
        return True
    elif A[n/2]-adj > n/2:
        return magicIndex(A[:n/2], adj)
    else: # A[n/2]-adj < n/2
        if (n==2): # Nothing to the right
            return False
        return magicIndex(A[n/2+1:], adj+n/2+1)

a = [0,2,3,4,5]
print checkForMagicIndex(a)

# If values could be duplicated - but still sorted - both left and right would need to be searched. 
# However, the less "dominant" side, the side which usually would be skipped, would only need to be searched up
# until Min(value, index-1) OR starting from Max(value, index+1).

# In this case it would also be easier to perform the recursion as A, start, end, instead of creating sub-lists
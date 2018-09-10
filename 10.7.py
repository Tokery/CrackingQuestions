# Read all integers from file into a bit array
# Scan through the bit array and find a 0
# Python is SUPER slow to allocate bits = ...

def findMissingInt(filename):
    MAX_VALUE = 2 ** 31
    bits = 2 ** MAX_VALUE

    file = open(filename, "r")
    for line in file:
        bits |= 1 << int(line)

    # for values 0 to MAX_VALUE
    for bit in range(MAX_VALUE + 1):
        if (bits >> bit & 1 == 0):
            return bit
    
    return -1

print(findMissingInt("107.txt"))
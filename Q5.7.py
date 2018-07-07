def swapEachPair(n):
    # This will only handle positive integers with up to 2^32-1
    oddBits = (n & 0xAAAAAAAA) >> 1
    evenBits = (n & 0x55555555) << 1
    return oddBits | evenBits

print swapEachPair(27)
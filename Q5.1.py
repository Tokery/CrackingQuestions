def insertion(n, m, i, j):
    left = (~0) << j
    right = (1 << i) - 1
    mask = left | right

    # clear space for the new number
    n = n & mask
    m = m << i
    return m | n

print insertion(1024,19,2,6)

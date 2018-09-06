# O(n) time, O(1) space
def triple_step(n):
    if (n == 1 or n == 2):
        return n
    elif n == 3:
        return 4

    n_3 = 1
    n_2 = 2
    n_1 = 4

    for i in range(4,n):
        new = n_1 + n_2  + n_3
        n_3 = n_2
        n_2 = n_1
        n_1 = new
    
    return n_1 + n_2 + n_3

print triple_step(5)
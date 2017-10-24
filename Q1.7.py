# Completed without using numpy
import copy as cp

def rotate90(arrOfArrs, n):
    n -= 1
    copy = cp.deepcopy(arrOfArrs)
    for x in range(0,n+1):
        for y in range(0, n+1):
            newY = x
            newX = n - y
            copy[newX][newY] = arrOfArrs[x][y]
    return copy


col1 = ['A', 'E', 'I', 'M']
col2 = ['B', 'F', 'J', 'N']
col3 = ['C', 'G', 'K', 'O']
col4 = ['D', 'H', 'L', 'P']
matrix = [col1, col2, col3, col4]

print (matrix)
print (rotate90(matrix, 4))
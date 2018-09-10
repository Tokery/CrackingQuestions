# Assumes both arrays are sorted
def sortedMerge(arrA, arrB, lenA, lenB):
    indexA = lenA - 1
    indexB = lenB - 1
    current = len(arrA) - 1

    while(indexA >= 0 and indexB >= 0):
        if (arrB[indexB] > arrA[indexA]):
            arrA[current] = arrB[indexB]
            current -= 1
            indexB -= 1
        else:
            arrA[current] = arrA[indexA]
            current -= 1
            indexA -= 1
    
    while (indexB >= 0):
        arrA[current] = arrB[indexB]
        current -= 1
        indexB -= 1

a = [1,4,7,8,9,11, None, None, None]
b = [8, 12, 14]
sortedMerge(a, b, 6, 3)
print(a)

a = [5, 11, 34, None, None, None]
b = [1, 3, 13]
sortedMerge(a, b, 3, 3)
print (a)


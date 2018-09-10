import math

def searchRotatedArray(arr, x, low, high):
    mid = math.floor((low + high) / 2)

    if (arr[mid] == x):
        return mid
    elif (x < arr[high] and x > arr[mid]):
        # Value is to the right 
        return searchRotatedArray(arr, x, mid + 1, high)
    else:
        return searchRotatedArray(arr, x, low, mid - 1)

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print (searchRotatedArray(arr, 5, 0, len(arr) - 1))
print (searchRotatedArray(arr, 19, 0, len(arr) - 1))

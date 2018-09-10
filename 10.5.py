import math

# OR could loop until find the next non blank entry
def sparseSearch(arr, x, low, high):
    mid = math.floor((low + high) / 2)

    # Search array has size 1
    if (low >= high and arr[mid] is not x):
        return 0

    if (arr[mid] == ""):
        return sparseSearch(arr, x, low, mid - 1) + sparseSearch(arr, x, mid + 1, high)
    elif (arr[mid] > x):
        return sparseSearch(arr, x, low, mid - 1)
    elif (arr[mid] < x):
        return sparseSearch(arr, x, mid + 1, high)
    else:
        return mid


arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print (sparseSearch(arr, "car", 0, len(arr)-1))
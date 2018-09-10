function binarySearch(arr, x) {
    let low = 0;
    let high = arr.length - 1;
    let mid = 0;

    // Don't forget plus and minus one since you know that the value at mid is not the required value
    while (low <= high) {
        mid = Math.floor((low + high) / 2);
        if (arr[mid] === x) {
            return mid;
        }
        else if (arr[mid] <  x) {
            low = mid + 1;
        }
        else if (arr[mid] > x) {
            high = mid - 1 ;
        }
    }
    return -1;
}

function binarySearchRecursive(arr, x, low, high) {
    if (low > high) return -1;

    const mid = Math.floor((low + high) / 2);

    if (arr[mid] === x) {
        return mid;
    }
    else if (arr[mid] < x) {
        return binarySearchRecursive(arr, x, mid + 1, high);
    }
    else if (arr[mid] > x) {
        return binarySearchRecursive(arr, x, low, mid - 1);
    }
}

const arr = [1,2,4,6,8,11,12,13,57,68,99];

console.log('Iterative', binarySearch(arr, 68));
console.log('Recursive', binarySearchRecursive(arr, 68, 0, arr.length - 1));
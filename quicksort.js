function quickSort(arr){
    quickSortInternal(arr, 0, arr.length-1);
}

function quickSortInternal(arr, left, right) {
    const pivotIndex = Math.floor((left + right) / 2);
    const index = pivot(arr, left, pivotIndex, right);

    // Don't sort arrays with one element
    if (left < index- 1) {
        quickSortInternal(arr, left, index - 1);
    }
    if (right > index) {
        quickSortInternal(arr, index, right);
    }
}

function pivot(arr, left, pivotIndex, right) {
    const pivot = arr[pivotIndex];

    while (left <= right) {
        // Get the next out of place item to the left of pivot
        while (arr[left] < pivot) left++;
        // Get the next out of place item to the right of pivot
        while (arr[right] > pivot) right--;

        // Only swap if the swap creates the right order
        if (left <= right) {
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
    return left;
}

const test = [3,2,6,1,9,10,8];
quickSort(test);
console.log(test);
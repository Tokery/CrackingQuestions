function mergesort(arr) {
    mergesortInternal(arr, [], 0, arr.length - 1);
}

function mergesortInternal(arr, tempArr, left, right) {
    if (left < right) {
        const middle = Math.floor((left + right) / 2);
        mergesortInternal(arr, tempArr, left, middle);
        mergesortInternal(arr, tempArr, middle + 1, right);
        merge(arr, tempArr, left, middle, right);
    }
}

function merge(arr, tempArr, left, middle, right) {
    console.log('merge', arr, left, middle, right);
    // Copy elements from arr into tempArr
    for (let i = left; i <= right; i++) {
        tempArr[i] = arr[i];
    }
    // Could use tempArr = arr.slice(left, right + 1) but this would technically use more space than required

    let current = left;
    let leftTemp = left;
    let rightTemp = middle + 1;
    while (leftTemp <= middle && rightTemp <= right) {
        if (tempArr[leftTemp] < tempArr[rightTemp]) {
            arr[current] = tempArr[leftTemp];
            leftTemp++;
        }
        else {
            arr[current] = tempArr[rightTemp];
            rightTemp++;
        }
        current++;
    }

    for (let i = leftTemp; i <= middle; i++) {
        arr[current] = tempArr[leftTemp];
        leftTemp++;
        current++;
    }
}

const test = [3,2,6,1,9,10,8];
mergesort(test);
console.log(test);
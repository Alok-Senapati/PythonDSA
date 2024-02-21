def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        # if arr[mid] == key:
        #     return mid
        if arr[mid] > key:
            if mid == 0 or (mid > 0 and arr[mid - 1] <= key):
                return mid
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        pos = binary_search(arr, 0, j, key)
        if pos == -1:
            continue
        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    arr1 = binary_sort([6, 8, 3, 9, 2, 1, 5, 10, 5])
    print(' '.join(map(str, arr1)))
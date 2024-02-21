def partition(arr, start, end):
    key = arr[start]
    i = start - 1
    j = end + 1
    while i < j:
        i += 1
        while i < len(arr) and arr[i] <= key:
            i += 1
        j -= 1
        while j >= 0 and arr[j] > key:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)

        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
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


arr = [6, 4, 5, 9, 3, 1]
print(quick_sort(arr, 0, len(arr) - 1))
print(' '.join(map(str, arr)))

print(binary_search(arr, 2))
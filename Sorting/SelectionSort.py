def sel_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


if __name__ == '__main__':
    arr1 = sel_sort([6, 8, 3, 9, 2, 1, 5, 10, 5])
    print(' '.join(map(str, arr1)))

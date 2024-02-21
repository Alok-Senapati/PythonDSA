def insert(arr, i):
    temp = arr[i]
    i -= 1
    while i >= 0 and arr[i] > temp:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = temp


def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert(arr, i)
    return arr


if __name__ == '__main__':
    arr1 = insertion_sort([6, 8, 3, 9, 2, 1, 5, 10, 5])
    print(' '.join(map(str, arr1)))

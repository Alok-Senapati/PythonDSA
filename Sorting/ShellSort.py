def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        i = gap
        while i < len(arr):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            i += 1
        gap //= 2
    return arr


if __name__ == '__main__':
    arr1 = shell_sort([6, 8, 3, 9, 2, 1, 5, 10, 5])
    print(' '.join(map(str, arr1)))


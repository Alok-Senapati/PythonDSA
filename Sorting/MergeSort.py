def merge(arr1, arr2):
    i = j = 0
    output = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    while i < len(arr1):
        output.append(arr1[i])
        i += 1

    while j < len(arr2):
        output.append(arr2[j])
        j += 1

    return output


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (0 + len(arr)) // 2
    arr_1 = merge_sort(arr[0:mid])
    arr_2 = merge_sort(arr[mid:])
    return merge(arr_1, arr_2)


if __name__ == '__main__':
    arr = merge_sort([6, 8, 3, 9, 2, 1, 5, 10])
    print(' '.join(map(str, arr)))

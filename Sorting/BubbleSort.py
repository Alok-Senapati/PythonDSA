from random import randint
import time


def bubble_sort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = True
        if not flag:
            break
    return arr


if __name__ == '__main__':
    start = time.time()
    input_list = [randint(1, 100) for i in range(100000)]
    arr1 = bubble_sort(input_list)
    print(' '.join(map(str, arr1)))
    end = time.time()
    print(f"Execution Time : {end - start}")

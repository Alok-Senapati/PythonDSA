import math


def find_lowest_two_digit(num):
    res = -1
    for i in range(2, 10):
        if num % i == 0 and num // i < 10:
            res = i
            break

    res2 = num // res
    return -1 if res == -1 else str(res)+str(res2)


if __name__ == '__main__':
    print(find_lowest_two_digit(76))
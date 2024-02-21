from MatrixMultiplication import multiply_mat
from MatrixExponentiation import mat_exp


def fib(n):
    if n == 0 or n == 1:
        return n
    c_mat = [[1, 1], [1, 0]]
    f = [[1], [0]]
    res = multiply_mat(mat_exp(c_mat, n - 1), f)
    return res[0][0]


if __name__ == '__main__':
    for num in range(12):
        print(fib(num), end=" ")

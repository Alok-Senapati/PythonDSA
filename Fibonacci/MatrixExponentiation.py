from MatrixMultiplication import multiply_mat


def mat_exp(mat, p):
    if len(mat) != len(mat[0]):
        return -1
    res = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))]
    while p > 0:
        if p & 1:
            res = multiply_mat(res, mat)
        mat = multiply_mat(mat, mat)
        p //= 2
    return res


if __name__ == '__main__':
    eye = mat_exp([[1, 2, 1], [3, 4, 3], [3, 4, 5]], 3)
    for i in range(len(eye)):
        for j in range(len(eye)):
            print(eye[i][j], end=" ")
        print()


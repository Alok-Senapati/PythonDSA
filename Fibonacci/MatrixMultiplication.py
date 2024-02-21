def multiply_mat(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return -1
    res = [[0 for i in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


if __name__ == '__main__':
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    matrix2 = [[4, 6],
               [7, 5],
               [3, 6]]
    matrix3 = multiply_mat(matrix1, matrix2)
    for i in range(len(matrix3)):
        for j in range(len(matrix3[0])):
            print(matrix3[i][j], end=' ')
        print()

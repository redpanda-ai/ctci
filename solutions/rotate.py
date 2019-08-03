matrix_5 = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

matrix_1 = [[1]]
matrix_2 = [[1, 2], [3, 4]]
matrix_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_0 = None

def rotate_right(matrix):
    if not matrix:
        return

    dim = len(matrix[0])

    for i in range(0, dim//2):
        rotate_shell(matrix, i)


def swap(matrix, x, y):
    matrix[x[0]][x[1]], matrix[y[0]][y[1]] = matrix[y[0]][y[1]], matrix[x[0]][x[1]]


def rotate_piece(matrix, first, last, i):
    t = matrix[first][first + i]
    matrix[first][first + i] = matrix[last - i][first]
    matrix[last - i][first] = matrix[last][last - i]
    matrix[last][last - i] = matrix[first + i][last]
    matrix[first + i][last] = t

def print_matrix(matrix):
    print("\n")
    if not matrix:
        return

    for line in matrix:
        print(line)


def rotate_shell(matrix, offset):
    first, last = 0 + offset, len(matrix[0]) - offset - 1

    for i in range(first, last):

        rotate_piece(matrix, first, last, i)

matrices = [matrix_0, matrix_1, matrix_2, matrix_3, matrix_5]

for matrix in matrices:
    print_matrix(matrix)
    rotate_right(matrix)
    print_matrix(matrix)


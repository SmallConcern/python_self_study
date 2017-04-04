
class InvalidMatrix(Exception):
    pass

def print_matrix(matrix):
    print('')
    for row in matrix:
        print(row)

def rotate_matrix(matrix):
    if not matrix or not matrix[0] or len(matrix) != len(matrix[0]):
        raise InvalidMatrix("Invalid matrix provided as input: {}".format(matrix))
    print_matrix(matrix)
    length = len(matrix)
    for layer in range(length/2):
        print("LAYER: {}".format(layer))
        first = layer
        last = length - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first] # left to top
            matrix[last-offset][first] = matrix[last][last-offset] # bottom to left
            matrix[last][last-offset] = matrix[i][last] # right to bottom
            matrix[i][last] = top
            print_matrix(matrix)


class TestMatrixRotation(object):
    def test_matrix_rotation(self):
        m = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
        print rotate_matrix(m)
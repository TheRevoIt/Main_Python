class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        for a in self.matrix:
            for number in a:
                print(number, end=' ')
            print()
        return ''

    def __add__(self, other):
        return Matrix([[i+n for i, n in zip(a, b)] for a, b in zip(self.matrix, other.matrix)])


matrix = [[5, 4], [1, 2], [2, 2]]
matrix2 = [[2, 3], [3, 4], [2, 7]]
a = Matrix(matrix)
b = Matrix(matrix2)
print(a+b)

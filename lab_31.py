import random

class MatrixDimensionError(Exception):
    """Класс для исключений, связанных с несовместимостью размеров матриц."""
    pass

class Matrix:
    def __init__(self, rows, cols, fill_random=False, min_val=0, max_val=10):
        self.rows = rows
        self.cols = cols
        if fill_random:
            self.data = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError("Матрицы должны быть одного размера для сложения.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError("Матрицы должны быть одного размера для вычитания.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise MatrixDimensionError(
                "Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы для умножения.")
        result = Matrix(self.rows, other.cols)
        result.data = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        result.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return result

    @staticmethod
    def concat(matrix1, matrix2, axis=1):
        if axis == 1 and matrix1.rows != matrix2.rows:
            raise MatrixDimensionError("Матрицы должны иметь одинаковое количество строк для конкатенации по столбцам.")
        if axis == 0 and matrix1.cols != matrix2.cols:
            raise MatrixDimensionError("Матрицы должны иметь одинаковое количество столбцов для конкатенации по строкам.")

        if axis == 1:
            result = Matrix(matrix1.rows, matrix1.cols + matrix2.cols)
            result.data = [matrix1.data[i] + matrix2.data[i] for i in range(matrix1.rows)]
        else:
            result = Matrix(matrix1.rows + matrix2.rows, matrix1.cols)
            result.data = matrix1.data + matrix2.data

        return result

    def apply_function(self, func):
        result = Matrix(self.rows, self.cols)
        result.data = [[func(self.data[i][j]) for j in range(self.cols)] for i in range(self.rows)]
        return result


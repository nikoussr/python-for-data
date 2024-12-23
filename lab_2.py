import random
from time import perf_counter_ns


class MatrixError(Exception):
    pass


class Matrix:
    def __init__(self, rows: int = 3, cols: int = 3, fill_random: bool = True, min_val: int = -10, max_val: int = 10):

        self.rows = rows
        self.cols = cols
        if fill_random:
            self.data = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_data(self, data: list[[int]]):
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
        self.data = data

    """Переопределенная функция сложения"""
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("Матрицы должны быть одного размера!")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)
        ]
        m1 = Matrix()
        m1.set_data(result)
        return m1

    """Переопределенная функция вычитания"""
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("Матрицы должны быть одного размера!")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)
        ]
        m1 = Matrix()
        m1.set_data(result)
        return m1

    """Переопределенная функция умножения"""
    def __mul__(self, other):
        if self.cols != other.rows:
            raise MatrixError("Количество столбцов A должно быть равно количество строк B!")
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in
            range(self.rows)
        ]
        m1 = Matrix()
        m1.set_data(result)
        return m1

    """Переопределенная функция вывода на экран"""
    def __str__(self):
        result = "\n".join([' '.join(map(str, row)) for row in self.data])
        return f"{result}\n"

    """Функция транспонирования"""
    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        m1 = Matrix()
        m1.set_data(transposed_data)
        return m1






def main():
    m1 = Matrix(rows=3, cols=6, fill_random=True, min_val=0, max_val=1)
    m2 = Matrix(rows=1, cols=1, fill_random=True, min_val=0, max_val=1)
    m3 = Matrix()
    print(m3)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('EXIT')

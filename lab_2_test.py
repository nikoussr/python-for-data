from lab_2 import Matrix, MatrixError
import unittest


class TestMathOperations(unittest.TestCase):
    def test_sum(self):
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)
        m3 = (m1+m2)
        self.assertAlmostEqual(m3.data,  (m1+m2).data)

    def test_sub(self):
        m1 = Matrix(4, 3)
        m2 = Matrix(4, 3)
        m3 = (m1 - m2)
        self.assertAlmostEqual(m3.data, (m1 - m2).data)

    def test_mul(self):
        m1 = Matrix(4, 3)
        m2 = Matrix(3, 60)
        m3 = (m1 * m2)
        self.assertAlmostEqual(m3.data, (m1 * m2).data)

    def test_matrix_error_1(self):
        with self.assertRaises(MatrixError):
            m1 = Matrix(4, 2)
            m2 = Matrix(4, 3)
            print(m1 + m2)

    def test_matrix_error_2(self):
        with self.assertRaises(MatrixError):
            m1 = Matrix(4, 2)
            m2 = Matrix(4, 3)
            print(m1 - m2)

    def test_matrix_error_3(self):
        with self.assertRaises(MatrixError):
            m1 = Matrix(12, 43)
            m2 = Matrix(42, 99)
            print(m1 * m2)

    def test_transpose(self):
        m1 = Matrix(12, 3)
        m1_transposed = m1.transpose()
        self.assertAlmostEqual(m1.cols, m1_transposed.rows)
        self.assertAlmostEqual(m1.rows, m1_transposed.cols)
        self.assertAlmostEqual(m1.data, m1_transposed.transpose().data)
        self.assertAlmostEqual(m1.cols, m1_transposed.transpose().cols)
        self.assertAlmostEqual(m1.rows, m1_transposed.transpose().rows)


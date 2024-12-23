from lab_1 import Matrix, add, subtract, multiply, divide
import unittest
import decimal


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(add(-1.5, 1.5), 0.0)
        self.assertAlmostEqual(add(-1.5, -2.5), -4.0)
        self.assertAlmostEqual(add(2.212, -0.212), 2.0)

    def test_subtract(self):
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(subtract(-1.5, -1.5), 0.0)
        self.assertAlmostEqual(subtract(0.0, 1.0), -1.0)

    def test_multiply(self):
        self.assertAlmostEqual(multiply(2.0, 3.0), 6.0)
        self.assertAlmostEqual(multiply(-1.0, 1.0), -1.0)
        self.assertAlmostEqual(multiply(0.0, 100.0), 0.0)
        self.assertAlmostEqual(multiply(1.13123, 332.1), 375.681483)

    def test_divide(self):
        self.assertAlmostEqual(divide(10.0, 2.0), 5.0)
        self.assertAlmostEqual(divide(-10.0, -2.0), 5.0)
        self.assertAlmostEqual(divide(10.0, 3.0), 10.0 / 3.0)
        self.assertAlmostEqual(divide(355.0, 113.0), 3.1415929203539825)
        self.assertAlmostEqual(divide(3.0, 13.0), 0.23076923076923078)

    def test_m_sum(self):
        data_1 = [
            [1, 2, 3],
            [1, 2, 3],
            [5, 5, 5]
        ]
        data_2 = [
            [0, 2, 3],
            [1, 2, 3],
            [2, 3, -5]
        ]
        m_1 = Matrix(data_1)
        m_2 = Matrix(data_2)
        self.assertAlmostEqual((m_1 + m_2).data, [[1, 4, 6], [2, 4, 6], [7, 8, 0]])

    def test_m_mult(self):
        data_1 = [
            [1, 100, 100],
            [100, 1, 100],
            [100, 100, 1]
        ]
        data_2 = [
            [2],
            [2],
            [2]
        ]
        m_1 = Matrix(data_1)
        m_2 = Matrix(data_2)
        self.assertAlmostEqual((m_1 * m_2).data, [[402], [402], [402]])

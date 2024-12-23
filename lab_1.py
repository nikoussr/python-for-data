import decimal
from decimal import Decimal


class MatrixError(Exception):
    pass


class DecimalError(Exception):
    pass


class Matrix:
    def __init__(self, data: list[list[int]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("Матрицы должны быть одного размера!")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("Матрицы должны быть одного размера!")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise MatrixError("Количество столбцов A должно быть равно количество строк B!")
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in
            range(self.rows)
        ]
        return Matrix(result)

    def __str__(self):
        return "\n".join([' '.join(map(str, row)) for row in self.data])


def input_matrix(rows, cols):
    data = []
    print(f"Введите элементы матрицы размером {rows}x{cols}:")
    for i in range(rows):
        while True:
            try:
                elements = get_all_int(f"Введите строку {i + 1} (через пробел): ")
                if len(elements) != cols:
                    raise MatrixError(
                        f"Ошибка: В строке {i + 1} должно быть {cols} элементов, а введено {len(elements)}.")

                data.append(elements)
                break  # Выход из цикла, если ввод корректен
            except MatrixError as e:
                print(e)
            except ValueError as e:
                print(e)

    return Matrix(data)


def add(x, y):
    return float(Decimal(str(x)) + Decimal(str(y)))


def subtract(x, y):
    return float(Decimal(x) - Decimal(y))


def multiply(x, y):
    return float(Decimal(x) * Decimal(y))


def divide(x, y):
    try:
        return float(Decimal(x) / Decimal(y))
    except decimal.DivisionByZero:
        print("Нельзя делить на ноль.")


def get_float(text: str) -> float:
    while True:
        user_input = input(text)
        try:
            value = float(user_input)
            if value != value or value == float('inf') or value == float('-inf'):
                raise ValueError
            return value
        except ValueError:
            print("Введено невещественное число")


def get_int(text: str) -> int:
    while True:
        user_input = input(text)
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                raise ValueError
        except ValueError:
            print("Введено не целое число или оно меньше нуля")

def get_all_int(text: str) -> list[int]:
    row = input(text)
    elements = row.split()

    # Проверка на наличие некорректных элементов
    for element in elements:
        try:
            int(element)  # Пробуем преобразовать элемент в целое число
        except ValueError:
            raise ValueError("Ошибка: Вводите только целые числа (включая отрицательные).")

    return [int(element) for element in elements]

def main():
    while True:
        operation = input("Выберите режим работы:\n"
                          "1 - Операции с числами\n"
                          "2 - Операции с матрицами\n"
                          "Введите номер режима: ")
        if operation == '1':
            while True:
                print("Выберите операцию с числами:\n"
                      "1 - Сложение\n"
                      "2 - Вычитание\n"
                      "3 - Умножение\n"
                      "4 - Деление\n"
                      "Введите номер операции: ")
                option = input()
                if option == '1':
                    first_float = get_float("Введите первое число: ")
                    second_float = get_float("Введите второе число: ")
                    result = add(first_float, second_float)
                    print(f"Результат {result}\n")
                    break
                elif option == '2':
                    first_float = get_float("Введите первое число: ")
                    second_float = get_float("Введите второе число: ")
                    result = subtract(first_float, second_float)
                    print(f"Результат {result}\n")
                    break
                elif option == '3':
                    first_float = get_float("Введите первое число: ")
                    second_float = get_float("Введите второе число: ")
                    result = multiply(first_float, second_float)
                    print(f"Результат {result}\n")
                    break
                elif option == '4':
                    first_float = get_float("Введите первое число: ")
                    second_float = get_float("Введите второе число: ")
                    result = divide(first_float, second_float)
                    print(f"Результат {result}\n")
                    break
                else:
                    print(f"Ошибка: Введите 1, 2, 3 или 4!")
        elif operation == '2':
            while True:
                print("Выберите операцию с матрицами:\n"
                      "1 - Сложение\n"
                      "2 - Умножение\n"
                      "Введите номер операции: ")
                option = input()
                if option == '1':
                    n = get_int(f"Введите количество строк первой матрицы: ")
                    m = get_int(f"Введите количество столбцов первой матрицы: ")
                    mat_1 = input_matrix(n, m)
                    k = get_int(f"Введите количество строк второй матрицы: ")
                    t = get_int(f"Введите количество столбцов второй матрицы: ")
                    mat_2 = input_matrix(k, t)
                    try:
                        result = mat_1 + mat_2
                        print(f"Результат: \n{result}\n")
                    except MatrixError as e:
                        print(e)
                    break
                elif option == '2':
                    n = get_int(f"Введите количество строк первой матрицы: ")
                    m = get_int(f"Введите количество столбцов первой матрицы: ")
                    mat_1 = input_matrix(n, m)
                    k = get_int(f"Введите количество строк второй матрицы: ")
                    t = get_int(f"Введите количество столбцов второй матрицы: ")
                    mat_2 = input_matrix(k, t)
                    try:
                        result = mat_1 * mat_2
                        print(f"Результат: \n{result}\n")
                    except MatrixError as e:
                        print(e)
                    break
        else:
            print(f"Ошибка: Введите 1 или 2!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nEXIT')

import time
import numpy as np
from lab_31 import Matrix
from sklearn.datasets import load_breast_cancer
from scipy.special import expit


class LogisticRegression_n:
    def __init__(self, x, y):
        self.intercept = np.ones((x.shape[0], 1))
        self.x = np.concatenate((self.intercept, x), axis=1)  # Используем NumPy для конкатенации
        self.weight = np.zeros(self.x.shape[1])
        self.y = y

    # Вычисление сигмоиды
    def sigmoid(self, x, weight):
        z = np.dot(x, weight)
        return 1 / (1 + np.exp(-z))

    # Вычисление функции потерь
    def loss(self, h, y):
        return -np.mean(y * np.log(h) + (1 - y) * np.log(1 - h))


    # Вычисление градиента
    def gradient_descent(self, X, h, y):
        return np.dot(X.T, (h - y)) / y.size

    # Функция обучения
    def fit(self, lr, iterations):
        for i in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            loss = self.loss(sigma, self.y)
            dW = self.gradient_descent(self.x, sigma, self.y)
            # Обновление весов
            self.weight -= lr * dW
        print('Fitted successfully to data')

    # Функция предсказания метки класса
    def predict(self, x_new, threshold):
        x_new = np.concatenate((self.intercept, x_new), axis=1)  # Используем NumPy для конкатенации
        result = self.sigmoid(x_new, self.weight)
        result = result >= threshold
        return result.astype(int)


class LogisticRegression_m:
    def __init__(self, x, y):
        self.intercept = Matrix(x.rows, 1)
        for i in range(self.intercept.rows):
            self.intercept.data[i][0] = 1
        self.x = Matrix.concat(self.intercept, x, axis=1)
        self.weight = Matrix(self.x.cols, 1)
        self.y = y

    def sigmoid(self, x, weight):
        z = x * weight
        result = Matrix(z.rows, z.cols)
        for i in range(z.rows):
            for j in range(z.cols):
                result.data[i][j] = 1 / (1 + np.exp(-z.data[i][j]))
        return result

    def loss(self, h, y):
        res2 = 0
        for i in range(h.rows):
            for j in range(h.cols):
                res2 += y.data[i][j] * np.log(h.data[i][j]) - (1 - y.data[i][j]) * np.log(1 - h.data[i][j])
        return -res2 / h.rows

    def gradient_descent(self, X, h, y):
        t_x = X.transpose()
        buf_res = Matrix(h.rows, h.cols)
        res = Matrix(X.cols, h.cols)
        for i in range(h.rows):
            for j in range(h.cols):
                buf_res.data[i][j] = h.data[i][j] - y.data[i][j]
        buf_res = t_x * buf_res
        for i in range(res.rows):
            for j in range(res.cols):
                res.data[i][j] = buf_res.data[i][j] / X.rows
        return res

    def fit(self, lr, iterations):
        for _ in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            loss = self.loss(sigma, self.y)
            dW = self.gradient_descent(self.x, sigma, self.y)
            for i in range(self.weight.rows):
                for j in range(self.weight.cols):
                    self.weight.data[i][j] -= lr * dW.data[i][j]
        print('Fitted successfully to data')

    def predict(self, x_new, threshold):
        x_new = Matrix.concat(self.intercept, x_new, axis=1)
        result = self.sigmoid(x_new, self.weight)
        y_pred = Matrix(result.rows, 1)
        for i in range(result.rows):
            y_pred.data[i][0] = 1 if result.data[i][0] >= threshold else 0
        return y_pred


def measure_performance():
    data = load_breast_cancer()
    x = data.data
    y = data.target
    start_time = time.time()
    regressor_n = LogisticRegression_n(x,y)
    regressor_n.fit(0.1, 1000)
    y_pred = regressor_n.predict(x, 0.5)
    end_time = time.time()
    print('Аccuracy: {:.3f}'.format(sum(y_pred == y) / len(y.data)))
    print(f"Время обучения с numpy - {round(end_time - start_time, 3)} c.")

    x_m = data.data
    y_m = data.target.reshape(-1, 1)

    x = Matrix(x_m.shape[0], x_m.shape[1])
    x.data = x_m.tolist()

    y = Matrix(y_m.shape[0], y_m.shape[1])
    y.data = y_m.tolist()

    regressor_m = LogisticRegression_m(x, y)
    start_time = time.time()
    regressor_m.fit(lr=0.1, iterations=1000)
    y_pred = regressor_m.predict(x, threshold=0.5)
    end_time = time.time()
    correct = sum(1 for i in range(y.rows) if y_pred.data[i][0] == y.data[i][0])
    accuracy = correct / y.rows
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Время обучения с Matrix - {round(end_time - start_time, 3)} c.")



if __name__ == '__main__':
    measure_performance()





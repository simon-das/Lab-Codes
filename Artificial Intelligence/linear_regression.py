import numpy as np
import matplotlib.pyplot as plt

def coefficient(x, y):
    n = np.size(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    cross_deviation_sum = np.sum(x * y) - n * mean_x * mean_y
    square_deviation_sum = np.sum(x * x) - n * mean_x * mean_x
    b_1 = cross_deviation_sum / square_deviation_sum
    b_0 = mean_y - b_1 * mean_x

    return (b_0, b_1)

def plot_line( x, y, b):
    plt.scatter(x, y, color = "r")
    y_pred = b[0] + b[1] * x
    plt.plot( x, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 2, 4, 5, 7, 8, 3, 6, 9, 10 ])
b = coefficient( x, y)
print("The coefficients are : {} and {}".format(b[0], b[1]))
plot_line( x, y, b)

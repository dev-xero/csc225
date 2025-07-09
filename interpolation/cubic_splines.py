import matplotlib.pyplot as plt
import numpy as np


def cerp(x, y, X):
    x_points = np.array(x)
    y_points = np.array(y)
    n = len(x)

    y2 = find_second_derivative(x_points, y_points, n)

    X_dense = np.array(X)
    Y_dense = np.zeros_like(X_dense)

    for i, xi in enumerate(X_dense):
        j = find_interval(xi, x_points)
        h = x[j + 1] - x[j]
        A = (x[j + 1] - xi) / h
        B = (xi - x[j]) / h
        C = (A**3 - A) * h**2 / 6
        D = (B**3 - B) * h**2 / 6

        Y_dense[i] = A * y[j] + B * y[j + 1] + C * y2[j] + D * y2[j + 1]

    return Y_dense


def find_second_derivative(x, y, n):
    a = np.zeros(n)  # sub-diagonal
    b = np.zeros(n)  # diagonal
    c = np.zeros(n)  # super-diagonal
    d = np.zeros(n)  # right-hand side

    # Natural boundary conditions
    b[0], d[0] = 1.0, 0.0
    b[n - 1], d[n - 1] = 1.0, 0.0

    for i in range(1, n - 1):
        h_i = x[i] - x[i - 1]
        h_i1 = x[i + 1] - x[i]
        a[i] = h_i
        b[i] = 2 * (h_i + h_i1)
        c[i] = h_i1
        d[i] = 6 * ((y[i + 1] - y[i]) / h_i1 - (y[i] - y[i - 1]) / h_i)

    # Solve tri-diagonal system using Thomas algorithm
    return thomas_alg(a, b, c, d)


def thomas_alg(a, b, c, d):
    n = len(d)

    # Forward elimination
    for i in range(1, n):
        factor = a[i] / b[i - 1]
        b[i] -= factor * c[i - 1]
        d[i] -= factor * d[i - 1]

    # Back substitution
    x = np.zeros(n)
    x[n - 1] = d[n - 1] / b[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]

    return x


def find_interval(xi, x):
    if xi < x[0] or xi > x[-1]:
        raise ValueError("Out of cubic interpolation interval")

    # Since the array is sorted, we can use binary search
    left, right = 0, len(x) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if x[mid] <= xi:
            left = mid
        else:
            right = mid

    return left


def plot_cerp(x, y, X, Y):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, "o", label="Data Points", color="black")
    plt.plot(X, Y, "-", label="Cubic Spline", color="blue")
    plt.legend()
    plt.grid(True)
    plt.title("Cubic Spline Interpolation")
    plt.show()


def evaluate():
    header = "CUBIC INTERPOLATION (CERP) VIA CUBIC SPLINES"
    print(header)
    print("-" * len(header))

    x_points = [
        0.0,
        0.2,
        0.4,
        0.6,
        0.8,
        1.0,
        1.2,
        1.4,
        1.6,
        1.8,
        2.0,
        2.2,
        2.4,
        2.6,
        2.8,
    ]
    y_points = [
        10.0,
        11.216,
        11.728,
        11.632,
        11.024,
        10.0,
        8.656,
        7.088,
        5.392,
        3.664,
        2.0,
        0.496,
        -0.752,
        -1.648,
        -2.096,
    ]
    X_dense = np.linspace(0.0, 2.8, 100)
    Y_dense = cerp(x_points, y_points, X_dense)

    print("x:", x_points)
    print("y:", y_points)
    print("X range:", f"{X_dense[0]:.2f} to {X_dense[-1]:.2f}")
    print("Y range:", f"{Y_dense.min():.2f} to {Y_dense.max():.2f}")

    plot_cerp(x_points, y_points, X_dense, Y_dense)


if __name__ == "__main__":
    evaluate()

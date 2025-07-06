import matplotlib.pyplot as plt


def qerp(x, y, X):
    """
    Quadratic spline interpolation is a method of constructing
    smooth curves that pass through a set of data points. It is
    C0 and C1 continuous meaning that function and its first order
    derivative are both continuous.

    We use 2nd degree polynomials and a bit of Linear Algebra 
    (due) to having to solve derivatives.

    Formula:
    - Si(x) = ai(x-xi)^2 + bi(x-xi) + ci
    - Where:
        - Si(x): Spline i
        - ai, bi, ci: coefficients

    Constraints:
    - Interpolation: Each splines must pass through each data point
    - Continuity: Adjacent splines must meet smoothly
    - Additional: We need to set the first or last spline 2nd derivative to 0

    Algorithm:
    - For n data points, we need (n-1) quad polynomials
    - Linear system Ax = b:
        - 3(n-1) x 3(n-1) matrix A
        - Boundary condition: a0 = 0
        - Interpolation constraint: ci = yi and aihi^2 + bihi + ci = yi+1
        - Continuity constraint: 2aihi + bi = bi+1
    - Solve Ax = b using Gaussian elimination
    - Extract coefficients (ai, bi, ci) for each spline
    - Find which interval [xi, xi+1] contains x (assume ascending order)
    - Compute Si(x) = ai(x-xi)^2 + bi(x-xi) + ci
    """
    n = len(x)
    n_splines = n - 1
    size = 3 * n_splines

    # System: Ax = b
    A = [[0.0] * size for _ in range(size)]
    b = [0.0] * size
    row = 0

    A[row][0] = 1.0
    b[row] = 0.0
    row += 1

    # Interpolation for ci = yi
    for i in range(n_splines):
        A[row][3*i + 2] = 1.0
        b[row] = y[i]
        row += 1

    # Interpolation for aihi^2 + bihi + ci = yi+1
    # where h = x - xi
    for i in range(n_splines):
        h = x[i+1] - x[i]
        # ai -> bi -> ci
        A[row][3*i] = h*h
        A[row][3*i + 1] = h
        A[row][3*i + 2] = 1.0
        b[row] = y[i+1]
        # should move to next row
        row += 1

    # Continuity for 2aihi + bi = bi+1
    for i in range(n_splines - 1):
        h = x[i+1] - x[i]
        # 2aihi -> bi -> -bi+1
        A[row][3*i] = 2*h
        A[row][3*i + 1] = 1.0
        A[row][3*(i+1) + 1] = -1.0
        b[row] = 0.0
        # again, next row
        row += 1

    # Gaussian elimination for system Ax = b
    coeffs = gauss_solve(A, b)
    spline_coeffs = [(coeffs[3*i], coeffs[3*i + 1], coeffs[3*i + 2])
                     for i in range(n_splines)]

    # Compute Si(x) for each query point
    Y = []
    for xi in X:
        # locate segment
        segment = 0
        for i in range(n_splines):
            if xi <= x[i+1]:
                segment = i
                break

        # as per the formula
        a, b, c = spline_coeffs[segment]
        dx = xi - x[segment]
        val = a * dx * dx + b * dx + c
        Y.append(val)

    return Y


def gauss_solve(A, b):
    """
    Solve a system of linear equations using Gaussian Elimination
    Algorithm:
    - forward elimination
    - backward elimination
    """
    n = len(A)

    # Forward elimination
    for i in range(n):
        # pivot is the max row
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # zero all rows below current col
        for k in range(i+1, n):
            if A[i][i] != 0:
                factor = A[k][i] / A[i][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]

    # Backward elimination
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def plot_qerp(x_points, y_points, X_dense, Y_dense):
    plt.plot(x_points, y_points, "o", label="Data Points", color="Black")
    plt.plot(X_dense, Y_dense, "-", label="Quadratic Spline", color="Green")
    plt.legend()
    plt.title("Quadratic Spline Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


def evaluate():
    header = "\nQUADRATIC INTERPOLATION (QERP) VIA QUADRATIC SPLINES"
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
    X_dense = [
        0.0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18,
        0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38,
        0.4, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58,
        0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78,
        0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98,
        1.0, 1.02, 1.04, 1.06, 1.08, 1.1, 1.12, 1.14, 1.16, 1.18,
        1.2, 1.22, 1.24, 1.26, 1.28, 1.3, 1.32, 1.34, 1.36, 1.38,
        1.4, 1.42, 1.44, 1.46, 1.48, 1.5, 1.52, 1.54, 1.56, 1.58,
        1.6, 1.62, 1.64, 1.66, 1.68, 1.7, 1.72, 1.74, 1.76, 1.78,
        1.8, 1.82, 1.84, 1.86, 1.88, 1.9, 1.92, 1.94, 1.96, 1.98,
        2.0, 2.02, 2.04, 2.06, 2.08, 2.1, 2.12, 2.14, 2.16, 2.18,
        2.2, 2.22, 2.24, 2.26, 2.28, 2.3, 2.32, 2.34, 2.36, 2.38,
        2.4, 2.42, 2.44, 2.46, 2.48, 2.5, 2.52, 2.54, 2.56, 2.58,
        2.6, 2.62, 2.64, 2.66, 2.68, 2.7, 2.72, 2.74, 2.76, 2.78,
        2.8
    ]

    Y_dense = qerp(x_points, y_points, X_dense)

    print("x:", x_points)
    print("y:", y_points)
    print("X:", X_dense)
    print("Y:", Y_dense)

    plot_qerp(x_points, y_points, X_dense, Y_dense)


if __name__ == "__main__":
    evaluate()

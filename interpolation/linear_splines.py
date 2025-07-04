import matplotlib.pyplot as plt


def lerp(x, y, X):
    """
    Linear Interpolation (Lerp) via Linear Splines
    ======================================================================
    Linear interpolation is a curve-fitting method of approximating paths
    which much pass through points using straight lines. Properties include
    C0 continuity i.e. continuous about the function

    Idea:
    In Linear Spline Interpolation, you have three parameters:
    - x: independent variable datapoints
    - y: dependent variable datapoints
    - X: queries

    Algorithm:
    - Ensure that each point in the X query is in our x interval
    - Find the specific interval X_i is in
    - Use interpolation formula to calculate Y_i
    - Return the Y results array

    Output:
    - Y: results of interpolated X queries

    Formula:
    - y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    """

    Y = []
    for xi in X:
        if xi < x[0] or xi > x[-1]:
            raise ValueError(f"Value: {xi} is outside the interpolation range")

        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                x0, x1 = x[i], x[i + 1]
                y0, y1 = y[i], y[i + 1]
                yi = y0 + (y1 - y0) * (xi - x0) / (x1 - x0)
                Y.append(yi)
                break

    return Y


def evaluate():
    header = "LINEAR INTERPOLATION (LERP) VIA LINEAR SPLINES"
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
    Y_dense = lerp(x_points, y_points, X_dense)

    print("x:", x_points)
    print("y:", y_points)
    print("X:", X_dense)
    print("Y:", Y_dense)

    plt.plot(x_points, y_points, "o", label="Data Points", color="black")
    plt.plot(X_dense, Y_dense, "-", label="Linear Spline", color="red")
    plt.legend()
    plt.title("Linear Spline Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    evaluate()


def plot_lerp():
    pass


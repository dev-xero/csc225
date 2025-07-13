import numpy as np


def LU(A):
    """
    Applies LU Decomposition using Dolittle's Algorithm to factorize
    a square matrix A
    """
    N = len(A)
    U = A.copy()
    L = np.eye(N)

    for k in range(N):
        for j in range(k + 1, N):
            if U[k][k] == 0:
                raise Exception("Division by zero")

            factor = U[j][k] / U[k][k]
            L[j][k] = factor
            U[j] = U[j] - factor * U[k]

    return L, U


def solve(A, b):
    """
    Solves a system of linear equations by applying LU Decomposition
    and using Gaussian Elimination

    An arbitrary system of linear equations can be represented using
    a matrix, and two vectors to indicate the number of unknowns and
    coefficients

    Generally Ax = b

    Where:
    A represents the coefficients matrix
    x represents the unknowns x1, x2,...xn
    b represents the RHS constants

    This system can be solved by combining LU-Decomposition and Gaussian
    Elimination/Back substitution:

    A = LU
    Ly = b
    Ux = y

    Where:
    A represents your coefficients matrix
    L represents a lower triangular matrix (Dolittle's format)
    U represents an upper triangular matrix
    y represents intermediate vector for determining x
    x represents the final result i.e. the unknowns
    """
    N = len(A)
    L, U = LU(A)

    print(f"{'L:':<{8}} {L.tolist()}")
    print(f"{'U:':<{8}} {U.tolist()}")

    # Solve: Ly = b
    y = np.zeros(N)
    y[0] = b[0] / L[0][0]
    for i in range(N):
        sum_ = 0
        for j in range(i):
            sum_ += L[i][j] * y[j]

        y[i] = (b[i] - sum_) / L[i][i]

    print(f"{'y:':<{8}} {y.tolist()}")

    # Solve: Ux = y (back substitution)
    x = np.zeros(N)
    for k in range(N - 1, -1, -1):
        sum_ = 0
        for j in range(k + 1, N):
            sum_ += U[k][j] * x[j]

        x[k] = (y[k] - sum_) / U[k][k]

    print(f"{'x:':<{8}} {x.tolist()}")


def extrapolate_components(system):
    """
    System of equations where each array represents the coefficients
    of x1, x2,..., xn and the final element represents the RHS constant
    """
    N = len(system)

    entries = 0
    for eqn in system:
        for _ in range(len(eqn) - 1):
            entries += 1

    if N**2 != entries:
        raise Exception("Number of unknowns doesn't match number of linear equations")

    # Extract first n-1 coefficients from each row
    # This is the coefficients matrix A
    # Last entry in each eqn is the RHS column vector b
    A = np.zeros((N, N))
    for i in range(N):
        eqn = system[i]
        for j in range(len(eqn) - 1):
            A[i][j] = system[i][j]

    b = np.array([eqn[-1] for eqn in system])

    return A, b


def print_header():
    header = "SOLVING SYSTEMS OF LINEAR EQUATIONS"
    print("-" * len(header))
    print(header)
    print("-" * len(header))


def evaluate():
    system = np.array([[2, 3, 1], [1, -2, 4]])
    A, b = extrapolate_components(system)

    print_header()
    print(f"{'system:':<{8}} {system.tolist()}")
    print(f"{'A:':<{8}} {A.tolist()}")
    print(f"{'b:':<{8}} {b.tolist()}")

    solve(A, b)


if __name__ == "__main__":
    evaluate()

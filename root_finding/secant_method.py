import math


def secant_method(x_n, x_nm1, fx, epsilon, max_iter=100, iter=0):
    """
    The Secant method is a root finding algorithm
    that uses secant lines to better approximate the
    roots of a real function, f

    parameters:
    - x_n: initial value of x
    - x_nm1: value of x preceding x_n
    - fx: function of x

    formula:
    - x_np1 = x_n - f(x_n)/denominator
    - denominator = [f(x_n) - f(x_nm1)]/[(x_n - x_nm1)]
    """
    if iter >= max_iter:
        return x_n

    f_xn = fx(x_n)
    f_xnm1 = fx(x_nm1)

    # convergence check
    if abs(x_n - x_nm1) == 0:
        return x_n

    # zero-division check
    if abs(f_xn - f_xnm1) == 0:
        return x_n

    # x_np1 is the value of x superseding x_n
    x_np1 = x_n - f_xn * (x_n - x_nm1) / (f_xn - f_xnm1)

    if abs(x_np1 - x_n) < epsilon:
        return x_np1

    return secant_method(x_np1, x_n, fx, epsilon, max_iter, iter + 1)


if __name__ == "__main__":
    EPSILON = 1e-6

    test_cases = [
        {"fx": lambda x: 1 - (2 * x * math.pow(math.e, -x / 2)), "x_n": 2, "x_nm1": 1},
        {"fx": lambda x: 5 - math.pow(x, -1), "x_n": 2, "x_nm1": 1},
    ]

    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        x_n = test["x_n"]
        x_nm1 = test["x_nm1"]

        print("-" * 55)
        print(f"Problem {chr(65 + idx)}")
        print("-" * 55)
        print(f"- x_n: {x_n}")
        print(f"- x_nm1: {x_nm1}")

        root = secant_method(x_n, x_nm1, fx, EPSILON)
        print(f"- found root as {root}\n")

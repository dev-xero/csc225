def secant_method(x_n, x_nm1, fx, max_iter=100, iter=0):
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
        - demonimator = [f(x_n) - f(x_nm1)]/[(x_n - x_nm1)]
    """
    if (iter >= max_iter):
        return x_n

    x_np1 = x_n - fx(x_n)
    x_np1 /= (fx(x_n) - fx(x_nm1)) / (x_n - x_nm1)

    return secant_method(x_np1,x_n,fx, max_iter, iter + 1)


if __name__ == "__main__":
    # secant_method()

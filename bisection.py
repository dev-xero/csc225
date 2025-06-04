def bisection(f, a, b, epsilon):
    """
        Bisection is a root-finding method for continuous functions
        where we halve the search space/interval [a,b] continuously
        within a tolerance factor, epsilon

        the intervals are chosen such that there exists 0 between
        them i.e. a < c < b, for each iteration we move in the
        direction that preserves this order

        in essence, we are just performing binary search on real
        numbers within a tolerance threshold

        parameters:
        - f: function
        - a: first value of the interval
        - b: second value of the interval
        - epsilon: tolerance threshold
    """
    fa, fb = f(a), f(b)

    if fa * fb > 0:
        return -1

    c = (a + b) / 2
    fc = f(c)

    if abs(fc) < epsilon:
        return c

    if abs(b - a) < epsilon:
        return c

    elif samesign(fa, fc):
        return bisection(f, c, b, epsilon)

    elif samesign(fb, fc):
        return bisection(f, a, c, epsilon)


def samesign(x, y):
    return (x > 0 and y > 0) or (x < 0 and y < 0)


def main():
    header = "BISECTION TEST CASES:"
    print(header)
    print("-" * len(header))

    def f1(x):
        return 2*x**2 - 7*x + 6

    root = bisection(f1, 1, 2, 1e-6)
    print(f"- Root found: {root}")


main()

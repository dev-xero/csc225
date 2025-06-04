import math
import inspect


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

    if abs(fa) < epsilon:
        return a
    if abs(fb) < epsilon:
        return b
    if fa * fb > 0:
        raise Exception("Interval does not cross 0")

    c = (a + b) / 2
    fc = f(c)

    if abs(fc) < epsilon or abs(b - a) < epsilon:
        return c

    if fa * fc > 0:
        return bisection(f, c, b, epsilon)
    else:
        return bisection(f, a, c, epsilon)


def source(fx):
    """
        Helper function to get lambda source text
    """
    text = inspect.getsource(fx)
    text = text.strip()
    text = text.split("lambda x: ")[1]
    return text


if __name__ == "__main__":
    test_cases = [
        {"fx": lambda x: 1 - (2 * x * math.pow(math.e, -x/2)),
         "a": 0.1, "b": 2},
        {"fx": lambda x: 5 - math.pow(x, -1), "a": 0.1, "b": 0.3},
        {"fx": lambda x: math.pow(x, 3) - (2 * x) - 5, "a": 2, "b": 3},
        {"fx": lambda x: math.pow(math.e, x) - 2, "a": 0, "b": 2},
        {"fx": lambda x: x - math.pow(math.e, -x), "a": 0, "b": 1},
        {"fx": lambda x: math.pow(x, 6) - x - 1, "a": 1, "b": 2},
        {"fx": lambda x: math.pow(x, 2) - math.sin(x), "a": 0, "b": 1},
        {"fx": lambda x: math.pow(x, 3) - 2, "a": 1, "b": 2},
        {"fx": lambda x: x + math.tan(x), "a": -1, "b": 0},
        # {"fx": lambda x: 2 - (math.pow(x, -1) * math.log(x)), "a": 0.01, "b": 2},
        # the above can't be solved with bisection, tsk tsk
    ]

    EPSILON = 1e-6
    print("FINDING ROOTS USING BISECTION METHOD")
    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        a = test["a"]
        b = test["b"]

        print("-" * 55)
        print(f"Problem {chr(65 + idx)}")
        print("-" * 55)
        print(f"- f(x): {source(fx)}")
        print(f"- a: {a}")
        print(f"- b: {b}")

        root = bisection(fx, a, b, EPSILON)
        print(f"- found root as: {root}\n")

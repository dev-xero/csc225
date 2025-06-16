import math

from utils import print_header


def trapezoidal_rule(f, a, b, n=100, epsilon=1e-6):
    """
    Approximates the definite integral of function f from a to b
    using the trapezoidal rule with n intervals

    Formula:
    S_trap = h * sum(f(x+h) + f(x))/2

    - where:
    - h: distance between intervals (x+i - x)/n
    - n: number of required intervals

    Parameters:
    - f: function of x, anti derivative
    - a: lower limit
    - b: upper limit
    - n: intervals
    - epsilon: tolerance threshold
    """
    h = (b - a) / n
    # for equal interval approximations, the endpoints
    # are halved
    summa = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        # this is the equivalent of moving i * h steps
        # from the start point, a
        x = a + i * h
        summa += f(x)

    return summa * h


def evaluate():
    test_cases = [
        {"fx": lambda x: math.sin(x), "a": 0, "b": math.pi / 2, "desc": "math.sin(x)"},
        {
            "fx": lambda x: math.pow(math.e, x),
            "a": 0,
            "b": 2,
            "desc": "math.pow(math.e, x)",
        },
        {"fx": lambda x: math.pow(x, 3), "a": 0, "b": 3, "desc": "math.pow(x, 3)"},
    ]

    print("TRAPEZOIDAL RULE FOR NUMERICAL INTEGRATION\n")
    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        desc = test["desc"]
        a = test["a"]
        b = test["b"]
        print_header(idx, fx=desc, a=a, b=b)
        result = trapezoidal_rule(fx, a, b)
        print("- solution:", result)


if __name__ == "__main__":
    evaluate()
